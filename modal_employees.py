employee_data = {
    "Yaroslavov": {
        "employee_id": "Yaroslavov",
        "name": "Ярославов А.А.",
        "photoUrl": "../static/img/blue_logo.png",
        "achievements": "член корр. РАН",
        "interests": " ХУЙресы сотрудника 2...",
        "articles": []
    },
    "chernikova_elena": {
        "employee_id": "chernikova_elena",
        "name": "Черникова Е.В. (зам. зав. лаборатории) ",
        "photoUrl": "../static/img/blue_logo.png",
        "achievements": "д.х.н., профессор РАН",
        "interests": "Научные интересы сотрудника 1...",
        "articles": []
    },

    "jyrnoff": {
        "employee_id": "jyrnoff",
        "name": "Жирнов А.Е.",
        "photoUrl": "../static/img/blue_logo.png",
        "achievements": "к.х.н., зам. декана химфака",
        "interests": " ХУЙресы сотрудника 2...",
        "articles": []
    },
    "Sergeyev": {
        "name": "Сергеев В.Г.",
        "photoUrl": "../static/img/blue_logo.png",
        "achievements": "к.х.н., зам. декана химфака",
        "interests": " ХУЙресы сотрудника 2...",
        "articles": []
    },
    "pyshkina": {
        "name": "Пышкина О.А.",
        "photoUrl": "../static/img/blue_logo.png",
        "achievements": "к.х.н., зам. декана химфака",
        "interests": " ХУЙресы сотрудника 2...",
        "articles": []
    },
    "elit": {

        "name": "Литманович Е.А.",
        "photoUrl": "../static/img/blue_logo.png",
        "achievements": "к.х.н., зам. декана химфака",
        "interests": " ХУЙресы сотрудника 2...",
        "articles": []
    },
}

import pickle

with open('employees_modal.pkl', 'wb') as f:
    pickle.dump(employee_data, f)
