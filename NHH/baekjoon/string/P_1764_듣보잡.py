import sys

N, M = map(int, input().split())

not_heard_list = set([input() for _ in range(N)])
not_seen_list = set([input() for _ in range(M)])

not_heard_and_not_seen = not_heard_list.intersection(not_seen_list)
not_heard_and_not_seen = sorted(not_heard_and_not_seen)

print(len(not_heard_and_not_seen))
print("\n".join(not_heard_and_not_seen))