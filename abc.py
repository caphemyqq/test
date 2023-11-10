import random
import xml.etree.ElementTree as ET

def load_settings():
    tree = ET.parse('setting.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def save_settings(x1, x2, n):
    root = ET.Element('settings')
    ET.SubElement(root, 'x1').text = str(x1)
    ET.SubElement(root, 'x2').text = str(x2)
    ET.SubElement(root, 'n').text = str(n)
    tree = ET.ElementTree(root)
    tree.write('setting.xml')

def main():
    x1, x2, n = load_settings()
    target_number = random.randint(x1, x2)

    print("猜數字遊戲開始！")
    print(f"目標數字在 {x1} 到 {x2} 之間。")

    for _ in range(n):
        guess = int(input("請猜一個數字："))

        if guess == target_number:
            print("恭喜，你猜對了！")
            break
        elif guess < target_number:
            print("太低了，再試一次。")
        else:
            print("太高了，再試一次。")

    else:
        print(f"很抱歉，你已經猜了{n}次，仍然沒有猜對。正確答案是 {target_number}。")

if __name__ == "__main__":
    main()
