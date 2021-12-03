with open("day3_input") as f:
    numbers = [n.strip() for n in f.readlines()]

gamma_bits = []
epsilon_bits = []
for i in range(len(numbers[0])):
    bits = [n[i] for n in numbers]
    if max(bits, key=bits.count) == "0":
        gamma_bits.append("0")
        epsilon_bits.append("1")
    else:
        gamma_bits.append("1")
        epsilon_bits.append("0")

gamma = int("".join(gamma_bits), 2)
epsilon = int("".join(epsilon_bits), 2)

power_consumption = gamma * epsilon
print(power_consumption)


def bit_filter(nums: list, bit_index: int, use_max: bool):
    if len(nums) == 1:
        return nums[0]
    bits = [n[bit_index] for n in nums]
    condition = (
        (max(bits, key=bits.count) if use_max else min(bits, key=bits.count))
        if bits.count("0") != bits.count("1")
        else ("1" if use_max else "0")
    )
    nums = [n for n in nums if n[bit_index] == condition]
    return bit_filter(nums, bit_index + 1, use_max)


oxygen_gen = bit_filter(numbers, 0, True)
co2_scrub = bit_filter(numbers, 0, False)

gen_rate = int("".join(oxygen_gen), 2)
scrub_rate = int("".join(co2_scrub), 2)

life_support_rating = gen_rate * scrub_rate
print(life_support_rating)
