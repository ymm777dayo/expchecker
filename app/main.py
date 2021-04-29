import tkinter as tk

s="0"

# リセット
def btn_click():
  txt.delete(0, tk.END)

#表示
def btn2_click():
  s=txt.get()
  label2.config(text="1e"+str(len(s)))

# 初期化
root = tk.Tk()
root.iconbitmap(default="icon.ico")
root.title("Test")
root.geometry("400x300")

# 説明文
label1 = tk.Label(text=u"ENTER YOUR NUMBER")
label1.pack()

# 入力フォーム
txt = tk.Entry(width=50)
txt.pack()

# リセットボタン
btn = tk.Button(root, text="RESET", command = btn_click)
btn.pack()

#表示
btn2 = tk.Button(root, text="APPEAR", command = btn2_click)
btn2.pack()


label2 = tk.Label(text="ここに表示されます")
label2.pack()

# 起動
root.mainloop()
