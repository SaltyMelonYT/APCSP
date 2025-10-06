def convert(match):
    bits = "0"
    total = int(bits,2)

    while total < match:
        if bits[-1] == "0":
            bits += "1"
        else:
            bits += "0"

        total = int(bits, 2)
        print(f"total={total}, bits={bits}")

    print(f"Final total: {total}, bits: {bits}")

convert(14)
