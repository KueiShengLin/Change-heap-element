from math import floor


def change_element(h, item):

    (new_value, tag) = item
    for i, (s, n) in enumerate(h):
        if n == tag:
            now = i
            h[now] = (new_value, tag)

            while True:
                min_child = now * 2 + 1

                if now != 0:
                    parent = floor((now - 1) / 2)
                    if new_value < h[parent][0]:
                        swap(h, now, parent)
                        now = parent

                    if now == 0:
                        break

                if min_child < len(h):
                    # Check which child is min
                    if min_child + 1 <= len(h):
                        if h[min_child][0] > h[min_child + 1][0]:
                            min_child += 1

                    if new_value > h[min_child][0]:
                        swap(h, now, min_child)
                        now = min_child

                    else:
                        break
                else:
                    break


def swap(h, i, j):
    t = h[i]
    h[i] = h[j]
    h[j] = t


if __name__ == "__main__":
    from heapq import heappush
    H = []
    heappush(H, (1, "a"))
    heappush(H, (8, "b"))
    heappush(H, (5, "c"))
    heappush(H, (9, "d"))
    heappush(H, (7, "e"))
    change_element(H, (0, "e"))
    print(H)
#
