# 8
일단은 화면을 페이지 단위로 보여줘서 서버에서 한번에 가져오는 데이터의 양을 줄일 수 있을 것 같아.
여기서는 페이지네이션으로 구현할 수도 있고 무한스크롤을 사용해서 구현할 수도 있어.

데이터 베이스로 mysql을 사용하게 되면 디폴트로 InnoDB라는 스토리지 엔진을 사용할 수 있어.
InnoDB 스토리지 엔진의 특징으로 기본키를 기준으로 정렬된 값을 저장하고 있거든.
상세화면은 느리지 않다고 한걸보니 이미 키본기로 상세화면에 필요한 데이터를 가져오고 있겠네.
많은 개발자분들이 게시판에 대한 데이터 베이스를 설계할 때 자동으로 생성되는 값으로 기본키를 설정하곤하지.
첫 화면에 기본키를 기준으로 내림차순으로 보여주게 된다면 인덱스를 어떤 컬럼에 생성해야할지 고민할 필요는 없겠어. 왜냐하면 기본키에 대해서는 자동으로 인덱스를 생성해 주거든.

인덱스라는 것은 등록, 수정, 삭제에 대한 기능을 포기하고 조회 성능을 올린다고 할 수 있어.
만약 인덱스를 사용하지 않았다면 조회수를 수정하는데 성능상 손해를 볼 수 있어.
mysql에서는 데이터를 수정하기 전에 동시에 같은 행에 접근하는 동시성 문제를 해결하기 위해서 인덱스 단위로 잠금을 걸어.
만약 테이블에 인덱스를 사용하지 않았다면 하나의 게시글에 대해서 조회수를 수정하는데 테이블의 모든 행을 잠굴 수 있어.


# 10
customer -- 고객 테이블
- customer_id -> bigint auto_increment primary key
- email varchar(100) unique key
- name varchar(100)
- open_count int

customer_present_box -- 고객_선물상자 테이블
- customer_present_box_id -> auto_increment primary key
- customer_id -> foreign key(customer_id) references customer(customer_id)
- present_box_id -> foreign key(present_box_id) references present_box(present_box_id)

present_box -- 선물 상자 테이블
- present_box_id -> bigint auto_increment
- box_type varchar(5) -- FIRST, SECOND, THIRD
- universe_id varchar(30) -> foreign key(종목_id) references universe(universe_id)
- chance decimal(5,4)

universe -- 종목 테이블
- universe_id bigint auto_increment
- name varchar(100)

쿼리:
insert into universe(name) values('꽝');
insert into universe(name) values('다꽝전자');
insert into universe(name) values('백원전자');
insert into universe(name) values('천원전자');
insert into universe(name) values('만원전자');
insert into universe(name) values('십만전자');

insert into present_box(box_type, universe_id, chance) values('FISRT', 1, 0.5);
insert into present_box(box_type, universe_id, chance) values('FISRT', 2, 0.3);
insert into present_box(box_type, universe_id, chance) values('FISRT', 3, 0.15);
insert into present_box(box_type, universe_id, chance) values('FISRT', 4, 0.1);

사용자에게 보여줄 상자 세개를 가져오는 쿼리:
select present_box_id, chance, (select name from universe where universe_id = pb.universe_id) as universe_name
from present_box pb where box_type = 'FISRT' order by rand() limit 1
union all
select present_box_id, chance, (select name from universe where universe_id = pb.universe_id) as universe_name
from present_box pb where box_type = 'SECOND' order by rand() limit 1
union all
select present_box_id, chance, (select name from universe where universe_id = pb.universe_id) as universe_name
from present_box pb where box_type = 'THIRD' order by rand() limit 1;


사용자가 선물 선택했을 때 쿼리:
1. 이미 선택한 선물인지 확인
select pb.box_type
from customer c
    join customer_present_box cpb on c.customer_id = cpb.customer_id
    join present_box pb on cpb.present_box_id = pb.present_box_id
2. 선물 선택 표시
insert into customer_present_box(customer_id, present_box_id) values (customerId, presentBoxId);


설계 시 고려사항:
- 스케줄러를 사용하며 메일 정각마다 "update cutomer_table set open_count = 0" 쿼리를 배치처리할 수 있도록한다.


11
장애 발생 원인 1: monolithic구조이기 때문에 데이터베이스를 도메인별로 분리하지 않아서 전체 서비스에 장애가 발생했다.
해결 방안 1: msa구조로 변경하여 하나의 서버에 장애가 발생해서 전체 서버의 장애로 확장되는 것을 막을 수 있다. 도메인 별로 데이터 베이스 분리가 필요하다.

장애 발생 원인 2: 하나의 계좌개설이 완료되기 전에 다른 계좌개설 API를 요청할 수 있다.
해결 방안 2: 계좌개설 버튼을 최초로 눌렀을 때 해당 계좌개설이 완료되기 전에는 클라이언트 단에서 계좌개설 버튼을 비활성화하고 서버에서는 계좌 개설중인 상태를 RDMBS로 저장하지 않고 NoSQL 저장 후 개설 진행 중인 상태면 더 이상 진행할 수 없다는 응답을 준다.

장애 발생 원인 3: Row Lock이 많이 발생했다. 고객의 계좌 보유 여부 상태를 수정하기 위해서 인걸로 판단됨
해결 방안3: Mysql에서는 데이터 수정 시 행 단위의 lock이 아닌 인덱스 단위의 lock을 걸기 때문에 적절한 인덱스 생성으로 인덱스 단위의 lock을 유도