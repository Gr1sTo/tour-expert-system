import tkinter as tk
from tkinter import ttk


# -------ЛОГІКА ЕКСПЕРТНОЇ СИСТЕМИ-------

def calculate_result():
    budget = budget_var.get()
    season = season_var.get()
    rest_type = rest_type_var.get()
    sea = sea_var.get()
    children = children_var.get()
    excursions = excursions_var.get()
    active = active_var.get()
    health = health_var.get()
    comfort = comfort_var.get()
    long_trip = long_trip_var.get()
    calm_rest = calm_rest_var.get()

    countries = [
        "Туреччина",
        "Єгипет",
        "Греція",
        "Італія",
        "Чехія",
        "Карпати",
        "Закарпаття",
        "Трускавець",
        "Болгарія",
        "Чорногорія"
    ]

    scores = {country: 0 for country in countries}
    reasons = {country: [] for country in countries}

    def add_score(country_list, points, reason):
        for country in country_list:
            scores[country] += points
            reasons[country].append(reason)

    # Тип відпочинку
    if rest_type == "пляжний":
        add_score(
            ["Туреччина", "Єгипет", "Греція", "Болгарія", "Чорногорія"],
            3,
            "відповідає пляжному типу відпочинку"
        )

    if rest_type == "екскурсійний":
        add_score(
            ["Італія", "Чехія", "Греція", "Чорногорія"],
            3,
            "підходить для екскурсійного відпочинку"
        )

    if rest_type == "активний":
        add_score(
            ["Карпати", "Чорногорія", "Закарпаття"],
            3,
            "підходить для активного відпочинку"
        )

    if rest_type == "оздоровчий":
        add_score(
            ["Трускавець", "Закарпаття", "Карпати"],
            3,
            "підходить для оздоровчого відпочинку"
        )

    if rest_type == "сімейний":
        add_score(
            ["Туреччина", "Болгарія", "Греція", "Закарпаття", "Карпати"],
            3,
            "підходить для сімейного відпочинку"
        )

    # Море
    if sea == "так":
        add_score(
            ["Туреччина", "Єгипет", "Греція", "Болгарія", "Чорногорія"],
            3,
            "має море"
        )
    else:
        add_score(
            ["Карпати", "Закарпаття", "Трускавець", "Чехія"],
            1,
            "не потребує моря"
        )

    # Діти
    if children == "так":
        add_score(
            ["Туреччина", "Болгарія", "Греція", "Закарпаття", "Карпати"],
            2,
            "підходить для подорожі з дітьми"
        )

    # Екскурсії
    if excursions == "так":
        add_score(
            ["Італія", "Чехія", "Греція", "Чорногорія"],
            3,
            "має можливості для екскурсій"
        )

    # Активний відпочинок
    if active == "так":
        add_score(
            ["Карпати", "Чорногорія", "Закарпаття"],
            3,
            "має можливості для активного відпочинку"
        )

    # Оздоровлення
    if health == "так":
        add_score(
            ["Трускавець", "Закарпаття", "Карпати"],
            3,
            "має оздоровчий формат відпочинку"
        )

    # Бюджет
    if budget == "низький":
        add_score(
            ["Карпати", "Закарпаття", "Болгарія"],
            2,
            "відповідає низькому бюджету"
        )

    elif budget == "середній":
        add_score(
            ["Туреччина", "Єгипет", "Греція", "Чехія", "Чорногорія", "Закарпаття"],
            2,
            "відповідає середньому бюджету"
        )

    elif budget == "високий":
        add_score(
            ["Італія", "Греція", "Туреччина"],
            2,
            "підходить для високого бюджету"
        )

    # Сезон
    if season == "літо":
        add_score(
            ["Туреччина", "Греція", "Болгарія", "Чорногорія", "Карпати"],
            2,
            "підходить для літнього сезону"
        )

    elif season == "зима":
        add_score(
            ["Єгипет", "Карпати", "Закарпаття", "Трускавець"],
            2,
            "підходить для зимового сезону"
        )

    elif season in ["весна", "осінь"]:
        add_score(
            ["Італія", "Чехія", "Греція", "Єгипет", "Закарпаття"],
            2,
            "підходить для весняного або осіннього сезону"
        )

    # Комфорт
    if comfort == "високий":
        add_score(
            ["Туреччина", "Греція", "Італія"],
            2,
            "має високий рівень комфорту"
        )

    elif comfort == "середній":
        add_score(
            ["Єгипет", "Чехія", "Чорногорія", "Болгарія", "Закарпаття"],
            2,
            "відповідає середньому рівню комфорту"
        )

    elif comfort == "базовий":
        add_score(
            ["Карпати", "Болгарія"],
            1,
            "може відповідати базовому рівню комфорту"
        )

    # Далека подорож
    if long_trip == "ні":
        add_score(
            ["Карпати", "Закарпаття", "Трускавець", "Чехія", "Болгарія"],
            2,
            "не потребує далекої подорожі"
        )

    else:
        add_score(
            ["Єгипет", "Туреччина", "Греція"],
            1,
            "можливий варіант для далекої подорожі"
        )

    # Спокійний відпочинок
    if calm_rest == "так":
        add_score(
            ["Закарпаття", "Трускавець", "Болгарія", "Чорногорія", "Туреччина"],
            2,
            "підходить для спокійного відпочинку"
        )

    sorted_results = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    best_country = sorted_results[0][0]
    best_score = sorted_results[0][1]

    max_possible_score = 23
    percent = round((best_score / max_possible_score) * 100)

    result_text = f"Рекомендований напрям: {best_country}\n"
    result_text += f"Кількість балів: {best_score}\n"
    result_text += f"Рівень відповідності: {percent}%\n\n"

    result_text += "Пояснення вибору:\n"
    for reason in reasons[best_country]:
        result_text += f"• {reason}\n"

    result_text += "\nАльтернативні варіанти:\n"
    for country, score in sorted_results[1:4]:
        alt_percent = round((score / max_possible_score) * 100)
        result_text += f"• {country} — {score} балів, відповідність {alt_percent}%\n"

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result_text)
    result_box.config(state="disabled")


def reset_fields():
    budget_var.set("середній")
    season_var.set("літо")
    rest_type_var.set("пляжний")
    sea_var.set("так")
    children_var.set("ні")
    excursions_var.set("ні")
    active_var.set("ні")
    health_var.set("ні")
    comfort_var.set("середній")
    long_trip_var.set("так")
    calm_rest_var.set("так")

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")

# -------ІНТЕРФЕЙС-------

root = tk.Tk()
root.title("Експертна система туристичного агента")
root.geometry("900x650")
root.resizable(False, False)

# Основні кольори
BG_COLOR = "#f4f7fb"
CARD_COLOR = "#ffffff"
TITLE_COLOR = "#1f2937"
BUTTON_COLOR = "#2563eb"

root.configure(bg=BG_COLOR)

title = tk.Label(
    root,
    text="Експертна система туристичного агента",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg=TITLE_COLOR
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Оберіть параметри подорожі, а система підбере найкращий напрям відпочинку",
    font=("Arial", 11),
    bg=BG_COLOR,
    fg="#4b5563"
)
subtitle.pack(pady=5)

main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(pady=15, padx=20, fill="both", expand=True)

left_frame = tk.Frame(main_frame, bg=CARD_COLOR, padx=20, pady=20)
left_frame.grid(row=0, column=0, sticky="n", padx=10)

right_frame = tk.Frame(main_frame, bg=CARD_COLOR, padx=20, pady=20)
right_frame.grid(row=0, column=1, sticky="n", padx=10)


def create_select(parent, label_text, variable, values, row):
    label = tk.Label(
        parent,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg=CARD_COLOR,
        fg="#374151",
        anchor="w"
    )
    label.grid(row=row, column=0, sticky="w", pady=6)

    combo = ttk.Combobox(
        parent,
        textvariable=variable,
        values=values,
        state="readonly",
        width=28
    )
    combo.grid(row=row, column=1, pady=6, padx=10)
    return combo


# Змінні
budget_var = tk.StringVar(value="середній")
season_var = tk.StringVar(value="літо")
rest_type_var = tk.StringVar(value="пляжний")
sea_var = tk.StringVar(value="так")
children_var = tk.StringVar(value="ні")
excursions_var = tk.StringVar(value="ні")
active_var = tk.StringVar(value="ні")
health_var = tk.StringVar(value="ні")
comfort_var = tk.StringVar(value="середній")
long_trip_var = tk.StringVar(value="так")
calm_rest_var = tk.StringVar(value="так")


# Поля вибору
create_select(
    left_frame,
    "Бюджет:",
    budget_var,
    ["низький", "середній", "високий"],
    0
)

create_select(
    left_frame,
    "Сезон:",
    season_var,
    ["літо", "осінь", "зима", "весна"],
    1
)

create_select(
    left_frame,
    "Тип відпочинку:",
    rest_type_var,
    ["пляжний", "екскурсійний", "активний", "оздоровчий", "сімейний"],
    2
)

create_select(
    left_frame,
    "Потрібне море:",
    sea_var,
    ["так", "ні"],
    3
)

create_select(
    left_frame,
    "Подорож із дітьми:",
    children_var,
    ["так", "ні"],
    4
)

create_select(
    left_frame,
    "Цікавлять екскурсії:",
    excursions_var,
    ["так", "ні"],
    5
)

create_select(
    left_frame,
    "Активний відпочинок:",
    active_var,
    ["так", "ні"],
    6
)

create_select(
    left_frame,
    "Потрібне оздоровлення:",
    health_var,
    ["так", "ні"],
    7
)

create_select(
    left_frame,
    "Рівень комфорту:",
    comfort_var,
    ["базовий", "середній", "високий"],
    8
)

create_select(
    left_frame,
    "Далека подорож:",
    long_trip_var,
    ["так", "ні"],
    9
)

create_select(
    left_frame,
    "Спокійний відпочинок:",
    calm_rest_var,
    ["так", "ні"],
    10
)


# Кнопки
button_frame = tk.Frame(left_frame, bg=CARD_COLOR)
button_frame.grid(row=11, column=0, columnspan=2, pady=20)

calculate_btn = tk.Button(
    button_frame,
    text="Отримати рекомендацію",
    command=calculate_result,
    font=("Arial", 11, "bold"),
    bg=BUTTON_COLOR,
    fg="white",
    padx=15,
    pady=8,
    borderwidth=0,
    cursor="hand2"
)
calculate_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(
    button_frame,
    text="Очистити",
    command=reset_fields,
    font=("Arial", 11),
    bg="#e5e7eb",
    fg="#111827",
    padx=15,
    pady=8,
    borderwidth=0,
    cursor="hand2"
)
reset_btn.grid(row=0, column=1, padx=5)


# Результат
result_title = tk.Label(
    right_frame,
    text="Результат роботи системи",
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg=TITLE_COLOR
)
result_title.pack(anchor="w", pady=(0, 10))

result_box = tk.Text(
    right_frame,
    width=45,
    height=27,
    font=("Arial", 10),
    wrap="word",
    bg="#f9fafb",
    fg="#111827",
    relief="flat",
    padx=10,
    pady=10
)
result_box.pack()

result_box.insert(
    tk.END,
    "Тут з’явиться рекомендація після натискання кнопки."
)
result_box.config(state="disabled")