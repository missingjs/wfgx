import base64


latest_gfwlist = "latest-gfwlist.txt"
decoded_gfwlist = "gfwlist-decoded.txt"
myrules = "myrules.txt"
merged_list = "merged.txt"


def decode_list():
    with open(latest_gfwlist) as fp:
        content = fp.read()
    s = base64.b64decode(content).decode()
    
    with open(decoded_gfwlist, "wt") as outfp:
        outfp.write(s)
    
    print(f"{decoded_gfwlist} ready")


def append_myrules():
    with open(myrules) as infp, open(decoded_gfwlist, "at") as outfp:
        outfp.write("\n!---- My Rules Start ----\n")
        for line in infp:
            outfp.write(line)
        outfp.write("!---- My Rules End ----\n")
    print(f"append {myrules} after {decoded_gfwlist}")


def encode_newlist():
    with open(decoded_gfwlist) as fp:
        content = fp.read()
    
    bytes_data = base64.b64encode(content.encode())
    with open(merged_list, "wb") as outfp:
        size = len(bytes_data)
        line_size = 64
        for i in range(0, size, 64):
            line = bytes_data[i:i+line_size]
            outfp.write(line)
            outfp.write(b'\n')

    print(f"{merged_list} ok")


def main():
    decode_list()
    append_myrules()
    encode_newlist()


if __name__ == '__main__':
    main()
