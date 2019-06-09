local_280 = [0x79,0x12c97f,0x135f0f8,0x74acbc6,0x56c614e,0xffffffe2]
local_268 = [0x79,0x12c97f,0x135f0f8,0x74acbc6,0x56c614e,0xffffffe2]
local_288 = 0
g = input().split(' ')
for i in range(6):
    g[i] = int(g[i])
    local_268[i] = local_268[i] - g[i] + 1
for i in range(6):
    local_288 += local_268[i]

print(local_288)
print(local_288 - 2**32)
