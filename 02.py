#Day 02

with open('./02.txt') as myinput:
    boxes_raw = myinput.readlines()

boxes = [list(map(int, i.replace('\n', '').split('x'))) for i in boxes_raw]

required_wrapping_paper, required_ribbon = 0, 0
for box in boxes:
    lw = box[0] * box[1]
    wh = box[1] * box[2]
    hl = box[2] * box[0]
    required_wrapping_paper += 2 * (lw + wh + hl) + min(lw, wh, hl)
    required_ribbon += 2 * (box[0] + box[1] + box[2] - max(box[0], box[1], box[2])) + box[0] * box[1] * box[2]

#Part 1

print(required_wrapping_paper)

#Part 2

print(required_ribbon)
