from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'brownie': {
        'Темный шоколад, г' :100,
        'Сливочное масло, г': 180,
        'Коричневый сахар, г': 200,
        'Куриное яйцо, шт': 4,
        'Пшеничная мука, г': 100,
        'Грецкие орехи, г': 100,

    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_view(request, recipe):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {ingredient: quantity * servings for ingredient, quantity in DATA.get(recipe).items()},
    }
    return render(request, 'calculator/index.html',context)


