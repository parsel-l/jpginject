# Replace User with your pc username

import os
import PIL.Image
import io

os.chdir('C:\\Users\\User\\Desktop\\jpginject\\input')

print("--------------------------------")
print("JPG INJECT by parsel")
print("--------------------------------")
print('''1 - Inject Message
2 - Inject Photo
3 - Inject Executable

4 - Read Injected Message
5 - Read Injected Image
6 - Read Injected Executable
''')

method = input("Select injection method: ")

if method == '1':
    print("--------------------------------")
    print("Selected Method: 1")
    print("--------------------------------")
    text = input("Message to inject: ")
    b = bytes(text, encoding='utf-8')
    with open('input.jpg', 'ab') as f:
        f.write(b)
        print(f"IMAGE SUCCESFULLY INJECTED WITH FOLLOWING MESSAGE: {text}")

elif method == '2':
    print("--------------------------------")
    print("Selected Method: 2")
    print("--------------------------------")
    
    img = PIL.Image.open('input2.jpg')
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')

    with open('input.jpg', 'ab') as f:
        f.write(byte_arr.getvalue())
        print('IMAGE SUCCESFULLY INJECTED')

elif method == '3':
    print("--------------------------------")
    print("Selected Method: 3")
    print("--------------------------------")
    
    with open('input.jpg', 'ab') as f, open('input.exe', 'rb') as e:
        f.write(e.read())

        print("EXECUTABLE SUCCESSFULLY INJECTED")

elif method == '4':
    print("--------------------------------")
    print("Selected Method: 4")
    print("--------------------------------")

    with open('input.jpg', 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)
        decode = f.read()
        decoded = bytes.decode(decode)
        print("MESSAGE FOUND!")
        print(decoded)

elif method == '5':
    print("--------------------------------")
    print("Selected Method: 5")
    print("--------------------------------")

    with open('input.jpg', 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        
        f.seek(offset + 2)

        new_img = PIL.Image.open(io.BytesIO(f.read()))
        new_img.save("C:\\Users\\User\\Desktop\\jpginject\\output\\output.png")
        print("IMAGE SAVED TO OUTPUT FOLDER")

elif method == '6':
    print("--------------------------------")
    print("Selected Method: 6")
    print("--------------------------------")

    with open('input.jpg', 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)

        with open('C:\\Users\\User\\Desktop\\jpginject\\output\\output.exe', 'wb') as e:
            e.write(f.read())
