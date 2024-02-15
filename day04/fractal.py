import tkinter as tk

memo = [0 if i == 0 else 1 if i ==1 else None for i in range(100)]

def fibo_memoization(number: int, memo: list) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    if memo[number] is not None:
        return memo[number]

    result = fibo_memoization(number-1, memo) + fibo_memoization(number-2, memo)
    memo[number] = result

    return result

w = tk.Tk()
w.title("Fibonacci")
w.geometry("250x150")

lbl_display_fibonacci_result = tk.Label(w, text="Fibonacci by memoization")
en_input_number = tk.Entry(w)
btn_click = tk.Button(w, text="Click")

lbl_display_fibonacci_result.pack()
en_input_number.pack(fill = "x")
btn_click.pack(fill = "x")

w.mainloop()