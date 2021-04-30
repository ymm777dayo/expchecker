import tkinter as tk

s="0"

# リセット
def btn_click():
  txt.delete(0, tk.END)

#表示
def btn2_click():
  s=txt.get()
  if not s.isdigit() :
    label2.config(text="error:数字以外は入力できません\n")
    return
  s = int(s)
  if s > 10000 :
    label2.config(text="error:10^6以上は入力できません\n")
  else :
    s = 2**int(s)
    label2.config(text="1e"+str(len(str(s))-1)+"\n")

# 初期化
root = tk.Tk()
root.iconbitmap(default="icon.ico")
root.title("Test")
root.geometry("400x300")

# 説明文
label1 = tk.Label(text=u"\n2の何乗ですか？\n")
label1.pack()

# 入力フォーム
txt = tk.Entry(width=5)
txt.pack()

# 改行
label3 = tk.Label(text="\n")
label3.pack()

# リセットボタン
btn = tk.Button(root, text="RESET", command = btn_click)
btn.pack()

# 改行
label4 = tk.Label(text="\n")
label4.pack()

label2 = tk.Label(text="ここに表示されます\n")
label2.pack()

#表示
btn2 = tk.Button(root, text="DISPLAY", command = btn2_click)
btn2.pack()

# 起動
root.mainloop()
