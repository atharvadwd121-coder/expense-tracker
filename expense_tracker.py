
import matplotlib.pyplot as z

l = []

def a():
    s1 = "Enter amount spent: "
    x = input(s1)
    try:
        f = float(x)
    except:
        f = 0.0
    s2 = "Enter description: "
    y = input(s2)
    d = {}
    k1 = 'a'
    k2 = 'd'
    d[k1] = f
    d[k2] = y
    l.append(d)
    m = "Expense added!\n"
    print(m)

def b():
    n = len(l)
    z0 = 0
    if n == z0:
        m = "No expenses recorded.\n"
        print(m)
        return
    h = "\nList of expenses:"
    print(h)
    c = 1
    for i in l:
        k1 = 'a'
        k2 = 'd'
        v1 = i[k1]
        v2 = i[k2]
        s_idx = str(c)
        s_dot = ". ₹"
        s_val = str(v1)
        s_sep = " -- "
        s_des = str(v2)
        f_str = s_idx + s_dot + s_val + s_sep + s_des
        print(f_str)
        c = c + 1
    print()

def c():
    t = 0.0
    k = 'a'
    for i in l:
        v = i[k]
        t = t + v
    p1 = "\nTotal spent: ₹"
    p2 = str(t)
    p3 = "\n"
    msg = p1 + p2 + p3
    print(msg)

def d():
    n = len(l)
    z0 = 0
    if n == z0:
        m = "No expenses to plot!\n"
        print(m)
        return
    x = []
    y = []
    c = 1
    k = 'a'
    for i in l:
        v = i[k]
        y.append(v)
        x.append(c)
        c = c + 1
    m_style = 'o'
    z.plot(x, y, marker=m_style)
    t_str = "Expense Variation"
    z.title(t_str)
    x_lbl = "Expense Number"
    z.xlabel(x_lbl)
    y_lbl = "Amount (₹)"
    z.ylabel(y_lbl)
    g = True
    z.grid(g)
    z.show()

def e():
    r = True
    while r:
        t1 = "Expense Tracker"
        print(t1)
        o1 = "1. Add Expense"
        print(o1)
        o2 = "2. View Expenses"
        print(o2)
        o3 = "3. Show Total Spent"
        print(o3)
        o4 = "4. Plot Expenses Graph"
        print(o4)
        o5 = "5. Exit"
        print(o5)
        p = "Choose an option (1-5): "
        i = input(p)
        
        opt1 = '1'
        opt2 = '2'
        opt3 = '3'
        opt4 = '4'
        opt5 = '5'
        
        if i == opt1:
            a()
        elif i == opt2:
            b()
        elif i == opt3:
            c()
        elif i == opt4:
            d()
        elif i == opt5:
            bye = "Goodbye!"
            print(bye)
            r = False
            break
        else:
            err = "Invalid choice. Please try again.\n"
            print(err)

if __name__ == "__main__":
    e()
