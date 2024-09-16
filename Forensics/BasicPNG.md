# BasicPNG writeup by `whales`

### Analying the given file
The challenge provided us a corrupted file, with the byte structure resembling a PE32+ file.

![image](https://github.com/user-attachments/assets/b8648a99-009c-47dc-a431-bd6397941e5e)

Instead of null bytes `00`, the file contained `1B`. 
My first thought was that the byte values had been shifted. 
To reverse this, I tried to shift the bytes back by subtracting the shift value:
```python
def shift_bytes(byte_array, shift_value=0x1B):
    return bytes([(byte - shift_value) % 256 for byte in byte_array])

def main():
    input = r"C:\Users\ADMIN\Downloads\basic.png"
    output = r"C:\Users\ADMIN\Downloads\test.txt"
    with open(input, "rb") as f:
        data = f.read()
    shifted_data = shift_bytes(data)
    with open(output, "wb") as f:
        f.write(shifted_data)
if __name__ == "__main__":
    main()
```
However, this approach didn’t get the expected results.

There was another way to transform 1B into 00, is to XORing each byte of the file with 1B.
I used the following script:
```python
def xor_bytes(byte_array, key=0x1B):
    return bytes([byte ^ key for byte in byte_array])

def main():
    input = r"C:\Users\ADMIN\Downloads\basic.png"
    output = r"C:\Users\ADMIN\Downloads\test2.txt"

    with open(input, "rb") as f:
        data = f.read()

    xor_data = xor_bytes(data)

    with open(output, "wb") as f:
        f.write(xor_data)

if __name__ == "__main__":
    main()
```
After running this script, I got the original file.
Now come to the reverse engineering part:
![image](https://github.com/user-attachments/assets/64813f62-f869-4bc9-b418-0aedb94e0aa5)
