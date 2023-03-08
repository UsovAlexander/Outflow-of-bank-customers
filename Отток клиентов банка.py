#!/usr/bin/env python
# coding: utf-8

# Привет, Александр!)
# <br> Меня зовут Дуолан 👋 Буду проверять твой проект. Давай вместе доведем его до идеала 😉
# <br> Дальнейшее общение будет происходить на «ты», если это не вызывает никаких проблем.
# <br> Желательно реагировать на каждый мой комментарий («исправил», «не понятно как исправить ошибку», ...)
# <br> Пожалуйста, не удаляй мои комментарии, они будут необходимы для повторного ревью.
# 
# Комментарии будут в <font color='green'>зеленой</font>, <font color='blue'>синей</font> или <font color='red'>красной</font> рамках:
# 
# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b> Если все сделано отлично
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>⚠️ Совет:</b> Если можно немного улучшить
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>❌ Замечание:</b> Если требуются исправления
# </div>
# 
# Работа не может быть принята с красными комментариями.
# 
# -------------------
# 
# Будет очень хорошо, если ты будешь помечать свои действия следующим образом:
# 
# <div class="alert alert-block alert-info">
# <b>Комментарий студента:</b> ...
# </div>
# 
# <div class="alert alert-block alert-info">
# <b>Изменения:</b> Были внесены следующие изменения ...
# </div>

# <h1>Содержание<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Подготовка-данных" data-toc-modified-id="Подготовка-данных-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Подготовка данных</a></span><ul class="toc-item"><li><span><a href="#Проверка-дубликатов" data-toc-modified-id="Проверка-дубликатов-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Проверка дубликатов</a></span></li><li><span><a href="#Проверка-пропусков" data-toc-modified-id="Проверка-пропусков-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Проверка пропусков</a></span></li><li><span><a href="#Подготовка-признаков" data-toc-modified-id="Подготовка-признаков-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Подготовка признаков</a></span></li></ul></li><li><span><a href="#Исследование-задачи" data-toc-modified-id="Исследование-задачи-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Исследование задачи</a></span></li><li><span><a href="#Борьба-с-дисбалансом" data-toc-modified-id="Борьба-с-дисбалансом-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Борьба с дисбалансом</a></span><ul class="toc-item"><li><span><a href="#Проверим-модели-при-увеличении-выборки" data-toc-modified-id="Проверим-модели-при-увеличении-выборки-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Проверим модели при увеличении выборки</a></span></li><li><span><a href="#Проверим-модели-при-уменьшении-выборки" data-toc-modified-id="Проверим-модели-при-уменьшении-выборки-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Проверим модели при уменьшении выборки</a></span></li><li><span><a href="#Проверим-модели,-взвесив-классы-при-помощи-аргумента-class_weight" data-toc-modified-id="Проверим-модели,-взвесив-классы-при-помощи-аргумента-class_weight-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Проверим модели, взвесив классы при помощи аргумента class_weight</a></span></li></ul></li><li><span><a href="#Тестирование-модели" data-toc-modified-id="Тестирование-модели-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Тестирование модели</a></span><ul class="toc-item"><li><span><a href="#Протестируем-модель,-показавшую-лучшую-метрику-F1." data-toc-modified-id="Протестируем-модель,-показавшую-лучшую-метрику-F1.-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Протестируем модель, показавшую лучшую метрику F1.</a></span></li><li><span><a href="#Проверим-значение-метрики-AUC-ROC-лучшей-модели" data-toc-modified-id="Проверим-значение-метрики-AUC-ROC-лучшей-модели-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Проверим значение метрики AUC-ROC лучшей модели</a></span></li></ul></li><li><span><a href="#Общий-вывод" data-toc-modified-id="Общий-вывод-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Общий вывод</a></span></li></ul></div>

# # Отток клиентов

# Из «Бета-Банка» стали уходить клиенты. Каждый месяц. Немного, но заметно. Банковские маркетологи посчитали: сохранять текущих клиентов дешевле, чем привлекать новых.
# 
# Нужно спрогнозировать, уйдёт клиент из банка в ближайшее время или нет. Вам предоставлены исторические данные о поведении клиентов и расторжении договоров с банком. 
# 
# Постройте модель с предельно большим значением *F1*-меры. Чтобы сдать проект успешно, нужно довести метрику до 0.59. Проверьте *F1*-меру на тестовой выборке самостоятельно.
# 
# Дополнительно измеряйте *AUC-ROC*, сравнивайте её значение с *F1*-мерой.
# 
# Источник данных: [https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)

# ## Подготовка данных

# In[1]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt


# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# Импорт выглядит отлично 👍
# </div>

# In[2]:


df = pd.read_csv('/datasets/Churn.csv')


# In[3]:


df = df.drop(['Surname', 'RowNumber', 'CustomerId'], axis=1)


# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# Удалить неинформативные признаки - хорошее решение 👍
# </div>

# ### Проверка дубликатов

# In[4]:


df.duplicated().sum()


# ### Проверка пропусков

# In[5]:


df.isna().sum()


# In[6]:


df.describe()


# In[7]:


df[~df['Tenure'].isna()].describe()


# Основные характеристики датафрема не изменились при скрывании пропусков в столбце Tenure поэтому можем от них избавиться.

# In[8]:


df = df.dropna().reset_index(drop=True)


# <div class="alert alert-block alert-warning">
# <b>⚠️ Совет:</b>
# 
# Посмотри еще на такие варианты работы с пропусками:
# 
# 1. Распределение по годам использования банка практически ровное, если сейчас заменить 909 пропусков медианой, то мы увеличим в 2 раза значение для 5 лет. Это кажется некорректным. Можно сделать заполнение пропусков случайными числами, тогда мы снизим влияние на наше распределение.
# 
# 2. Так как значений в этом признаке ограниченное количество, можно сделать его категориальным признаком. Пропуски можно считать как за отдельную категорию (заполнить значением -1). Затем заменить тип данных Tenure на object и применить технику OHE.
# 
# 3. Заполнить "0", считая, что это новые клиенты.
# </div>

# <div class="alert alert-block alert-info">
# <b>Комментарий студента:</b> Я думал о разных способах заполнения пропусков в этом датасете, но из-за ситуации, которую ты описал в 1 пункте, все они для меня показались неудачными. Во избежании искусственного влияния на результат прогнозирования, я принял решение удалить пропуски. Не уверен, что оставшиеся два способа будут оптимальными, нужно поэксперементировать)
# </div>

# ### Подготовка признаков

# <div class="alert alert-block alert-info">
# <b>Изменения:</b> Преобразование признаков поставил после разбиения.
# </div>

# Разобьем датафрем на три выборки

# In[9]:


get_ipython().system('pip install fast_ml')
from fast_ml.model_development import train_valid_test_split

X_train, y_train, X_valid, y_valid, X_test, y_test = train_valid_test_split(df, target = 'Exited', 
                                                                            train_size=0.6, valid_size=0.2, test_size=0.2)


# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b> 
# 
# Данные поделены верно, пропорции выбраны адекватные 👍
# </div>

# Преобразуем категориальные признаки при помощи техники OHE

# <div class="alert alert-block alert-danger">
# <b>❌ Замечание:</b>
# 
# Кодировать данные стоит после разбиения. Так у нас не будет утечки данных.
# 
# Подробнее об этом можно прочитать здесь https://datascience.stackexchange.com/questions/108663/why-label-encoding-before-split-is-data-leakage
#   
# Суть в том, что в предобработке данных мы не должны заглядывать в тестовую выборку. Когда кодировщик fit-ится на всей выборке, там ведь есть и тестовая выборка, поэтому это называют утечкой или подглядыванием. 
# 
# P.S. после прямого кодирования кол-во столбцов в выборках может отличаться. Тогда лишние признаки можно удалить
# </div>
# 
# ```python
# features_train = pd.get_dummies(features_train, drop_first=True)
# features_valid = pd.get_dummies(features_valid, drop_first=True)
# features_test = pd.get_dummies(features_test, drop_first=True)
# ```

# <div class="alert alert-block alert-success">
# <b>V2 ✔️ Успешно исправлено</b>
# </div>

# In[10]:


X_train = pd.get_dummies(X_train, drop_first=True)
X_valid = pd.get_dummies(X_valid, drop_first=True)
X_test = pd.get_dummies(X_test, drop_first=True)


# In[16]:


X_train.head()


# In[17]:


X_valid.head()


# In[18]:


X_test.head()


# Потерь столбцов после кодирования не наблюдается. Масштабируем количественные признаки с разным разбросом значений

# In[19]:


numeric = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']

scaler = StandardScaler()
scaler.fit(X_train[numeric])
X_train[numeric] = scaler.transform(X_train[numeric])


# In[20]:


scaler.fit(X_valid[numeric])
X_valid[numeric] = scaler.transform(X_valid[numeric])


# In[22]:


scaler.fit(X_test[numeric])
X_test[numeric] = scaler.transform(X_test[numeric])


# <div class="alert alert-block alert-danger">
# <b>❌ Замечание:</b>
# 
# Масштабирование тоже должно выполняться после разбиения данных. Scaler обучаешь на тренировочной выборке, затем по очереди применяешь стандартизацию ко всем выборкам. Точно как в обучении моделей. Так мы сможем избежать утечки данных
# </div>

# <div class="alert alert-block alert-success">
# <b>V2 ✔️ Успешно исправлено</b>
# </div>

# ## Исследование задачи

# In[23]:


y_train.value_counts(normalize=True)


# В тренировочной выборке присутствует дисбаланс классов. Исследуем несколько моделей и проверим влияние дисбаланса на качество предсказания.

# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# Виден явный дисбаланс классов в пользу отрицательного класса. Если мы будем всех людей прогнозировать, что они не уйдут из банка, то в 80% случаев мы будем правы.
# </div>

# **Напишем функцию поиска лучшей модели**

# In[24]:


def clf_models(X_train, y_train, X_valid, y_valid):
    f1 = []
    depth_value = ['-']
    n_estimators_value = ['-', '-']
    models = []
    
    #Проверим логистическую регрессию
    model_lr = LogisticRegression(random_state=12345, solver='lbfgs', max_iter=1000)
    model_lr.fit(X_train, y_train) 
    y_pred = model_lr.predict(X_valid) 
    result = f1_score(y_valid, y_pred)
    f1.append(result)
    models.append(model_lr)
    
    #Проверим дерево решений
    best_model_dtc = None
    best_result = 0
    best_depth = 0
    for depth in range(1, 11):
        model = DecisionTreeClassifier(random_state=12345, max_depth=depth) 
        model.fit(X_train, y_train) 
        y_pred = model.predict(X_valid) 
        result = f1_score(y_valid, y_pred) 
        if result > best_result:
            best_model_dtc = model
            best_depth = depth
            best_result = result
    f1.append(result)
    depth_value.append(best_depth)
    models.append(best_model_dtc)
    
    #Проверим случайный лес
    best_model_rfc = None
    best_result = 0
    best_est = 0
    best_depth = 0
    for est in range(1, 101, 10):
        for depth in range (1, 11):
            model = RandomForestClassifier(random_state=12345, n_estimators=est, max_depth=depth) 
            model.fit(X_train, y_train) 
            y_pred = model.predict(X_valid) 
            result = f1_score(y_valid, y_pred) 
            if result > best_result:
                best_model_rfc = model
                best_result = result
                best_est = est
                best_depth = depth
    f1.append(result)
    depth_value.append(best_depth)
    n_estimators_value.append(best_est)
    models.append(best_model_rfc)
    

    df = pd.DataFrame({'clf':['Logic', 'Tree', 'Forest'], 'f1':f1, 'depth':depth_value, 
                       'n_estimators': n_estimators_value})
    print(df)

    fig, axes = plt.subplots(1, 3, figsize=(15,5))

    for model, ax in zip(models, axes.flatten()):
        plot_confusion_matrix(model, X_valid, y_valid, normalize='true', ax=ax, cmap='Blues')
        ax.title.set_text(type(model).__name__)
    plt.tight_layout()  
    plt.show()
    
    return models


# In[25]:


clf_models(X_train, y_train, X_valid, y_valid)


# **Вывод:** Опираясь на результаты предсказаний, выведенные с помощью матрицы ошибок, можно сделать вывод, что из-за дисбаланса TPR в лучшем случае составляет 0.49, а F1 не привышает 0,55, что нельзя назвать удовлетворительным результатом. Проверим данные модели, исправив дисбаланс классов.

# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# Модели обучены корректно 👍
# </div>

# ## Борьба с дисбалансом

# ### Проверим модели при увеличении выборки

# In[26]:


#Функция увеличения выборки
def upsample(X, y, repeat):
    X_zeros = X[y == 0]
    X_ones = X[y == 1]
    y_zeros = y[y == 0]
    y_ones = y[y == 1]

    X_upsampled = pd.concat([X_zeros] + [X_ones] * repeat)
    y_upsampled = pd.concat([y_zeros] + [y_ones] * repeat)
    
    X_upsampled, y_upsampled = shuffle(X_upsampled, y_upsampled, random_state=12345)
    
    return X_upsampled, y_upsampled


# In[27]:


X_train_up, y_train_up = upsample(X_train, y_train, 4)


# In[28]:


models_up = clf_models(X_train_up, y_train_up, X_valid, y_valid)


# **Вывод:** Все модели показали значительный рост в определении 1 класса, метрика F1 превысила значение 0,6.

# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# Увеличение выборки выполнено верно - классы сбалансированы 👍 
# </div>

# ### Проверим модели при уменьшении выборки

# In[29]:


# Функция уменьшения выборки
def downsample(X, y, fraction):
    X_zeros = X[y == 0]
    X_ones = X[y == 1]
    y_zeros = y[y == 0]
    y_ones = y[y == 1]

    X_downsampled = pd.concat([X_zeros.sample(frac=fraction, random_state=12345)] + [X_ones])
    y_downsampled = pd.concat([y_zeros.sample(frac=fraction, random_state=12345)] + [y_ones])
    
    X_downsampled, y_downsampled = shuffle(X_downsampled, y_downsampled, random_state=12345)
    
    return X_downsampled, y_downsampled

X_train_down, y_train_down = downsample(X_train, y_train, 0.2)


# In[30]:


models_down = clf_models(X_train_down, y_train_down, X_valid, y_valid)


# **Вывод:** TPR стал еще выше, однако, тоже самое нельзя сказать про F1, т.к. FP срабатываний стало больше.

# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# Уменьшение выборки тоже выполнено верно 👍 
# </div>

# ### Проверим модели, взвесив классы при помощи аргумента class_weight

# In[31]:


def clf_models_class_weight(X_train, y_train, X_valid, y_valid):
    f1 = []
    depth_value = ['-']
    n_estimators_value = ['-', '-']
    models = []
    
    #Проверим логистическую регрессию
    model_lr = LogisticRegression(random_state=12345, solver='lbfgs', max_iter=1000, class_weight='balanced')
    model_lr.fit(X_train, y_train) 
    y_pred = model_lr.predict(X_valid) 
    result = f1_score(y_valid, y_pred)
    f1.append(result)
    models.append(model_lr)
    
    #Проверим дерево решений
    best_model_dtc = None
    best_result = 0
    best_depth = 0
    for depth in range(1, 11):
        model = DecisionTreeClassifier(random_state=12345, max_depth=depth, class_weight='balanced') 
        model.fit(X_train, y_train) 
        y_pred = model.predict(X_valid) 
        result = f1_score(y_valid, y_pred) 
        if result > best_result:
            best_model_dtc = model
            best_depth = depth
            best_result = result
    f1.append(result)
    depth_value.append(best_depth)
    models.append(best_model_dtc)
    
    #Проверим случайный лес
    best_model_rfc = None
    best_result = 0
    best_est = 0
    best_depth = 0
    for est in range(1, 101, 10):
        for depth in range (1, 11):
            model = RandomForestClassifier(random_state=12345, n_estimators=est, max_depth=depth, class_weight='balanced') 
            model.fit(X_train, y_train) 
            y_pred = model.predict(X_valid) 
            result = f1_score(y_valid, y_pred) 
            if result > best_result:
                best_model_rfc = model
                best_result = result
                best_est = est
                best_depth = depth
    f1.append(result)
    depth_value.append(best_depth)
    n_estimators_value.append(best_est)
    models.append(best_model_rfc)
    
    df = pd.DataFrame({'clf':['Logic', 'Tree', 'Forest'], 'f1':f1, 'depth':depth_value, 
                       'n_estimators': n_estimators_value})
    print(df)

    fig, axes = plt.subplots(1, 3, figsize=(15,5))

    for model, ax in zip(models, axes.flatten()):
        plot_confusion_matrix(model, X_valid, y_valid, normalize='true', ax=ax, cmap='Blues')
        ax.title.set_text(type(model).__name__)
    plt.tight_layout()  
    plt.show()
    
    return models


# In[32]:


models_class_weight = clf_models_class_weight(X_train, y_train, X_valid, y_valid)


# **Вывод:** TPR хуже предыдущего метода борьбы с дисбалансом, хотя F1 лучше. 

# **Общий вывод: наилучший результат F1 метрики показал модель RandomForestClassifier, это говорит о наименьшем количестве ложных срабатываний при наибольшем для этой модели показателе FPR.**

# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# По модельной части замечаний нет!) Все этапы выполнены отлично 👍
# </div>

# ## Тестирование модели

# ### Протестируем модель, показавшую лучшую метрику F1.

# In[40]:


for model in models_up: 
    print(type(model).__name__, f1_score(y_test, model.predict(X_test)))


# **Вывод:** значение F1 на тестовой выборке у модели RandomForestClassifier выше 0.59, не идеально конечно, но с этим уже можно работать.

# <div class="alert alert-block alert-success">
# <b>✔️ Успех:</b>
# 
# Отличный результат 👍 
# </div>

# ### Проверим значение метрики AUC-ROC лучшей модели

# In[41]:


probabilities_test = model.predict_proba(X_test)
probabilities_one_test = probabilities_test[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, probabilities_one_test)

plt.figure()

plt.plot(fpr, tpr)

plt.plot([0, 1], [0, 1], linestyle='--')

plt.xlim([0,1])
plt.ylim([0,1])

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.grid()
plt.title("ROC-кривая")

plt.show()


# In[42]:


roc_auc_score(y_test, probabilities_one_test)


# Найдем разницу между TPR и FPR при разных порогах.

# In[43]:


df_roc = pd.DataFrame({'fpr': fpr, 'tpr':tpr, 'thresholds':thresholds})


# In[44]:


df_roc['tpr - fpr'] = df_roc['tpr'] - df_roc['fpr']


# In[45]:


df_roc.sort_values('tpr - fpr', ascending=False).head()


# **Вывод:** в зависимости от веса дохода (TPR) от удержания клиента и веса издержек (TPR) при ошибочном срабатывании можно определить оптимальный порог, при котором прибыль будет максимальной.

# In[46]:


print(f"""Если веса TPR и FPR одинаковые, то в нашем случае оптимальный порог составит 
{df_roc.sort_values('tpr - fpr', ascending=False)['thresholds'].head(1)}""")


# <div class="alert alert-block alert-danger">
# <b>❌ Замечание:</b>
# 
# Осталось написать только финальный вывод)
#  
# Что можно добавить:
# 1. Краткий обзор выполненной работы
# 2. Конечный результат
# 3. Рекомендации для бизнеса (необязательно)
# </div>

# <div class="alert alert-block alert-info">
# <b>Изменения:</b> Добавил общий вывод
# </div>

# <div class="alert alert-block alert-success">
# <b>V2 ✔️ Успешно исправлено</b>
# </div>

# ## Общий вывод

# 1.Провели обучение трех моделей: LogisticRegression, DecisionTreeClassifier, RandomForestClassifier - на оригинальнйо выборке и сбалансированной. Балансировку провели тремя разными способами: с помощью аргумента class_weight, а также через увеличение и уменьшение выборки.
# 
# 2.Наилучший показатель метрики F1 показала модель RandomForestClassifier(max_depth=8, n_estimators=51, random_state=12345) при увеличенной тренировочной выборки. Результат на валидационной выборке по метрике F1 0.621787, на тестовой 0.627720. Модель в 71% случаев правильно определяет клиентов, которые уйдут, и 86% случаях, которые останутся.
# 
# 3.На данный момент 20% клиентов покидают банк, этот показатель можно сократить. Необходимо определить доход от удержаного клиента и издержки направленные на удержания клиента для определения оптимального порога, с помощью которого можно будет настроить модель для получения максимальной прибыли от удержания клиентов.

# # <font color='orange'>Общее впечатление</font>
# * Этот проект выполнен очень хорошо
# * Видно, что приложено много усилий
# * Молодец, что структурируешь ноутбук, приятно проверять такие работы
# * У тебя чистый и лаконичный код
# * Мне было интересно читать твои промежуточные выводы
# * Твой уровень подачи материала находится на высоком уровне
# * Исправь, пожалуйста, мои замечания. Затем отправляй на повторную проверку
# * Жду новую версию проекта 👋

# # <font color='orange'>2. Общее впечатление</font>
# * Спасибо за быстрое внесение правок
# * Теперь проект выглядит лучше )
# * Критических замечаний нет
# * Молодец, отличная работа!
# * Надеюсь, ревью было полезным
# * Удачи в дальнейшем обучении 👋

# # <font color='orange'>Рекомендации 🔥</font>
# * Анализ данных на python и pandas https://www.youtube.com/watch?v=dd3RcafdOQk&t=82s
# * Курс "Введение в машинное обучение" https://stepik.org/course/4852
# * Разумные способы кодирования категориальных данных для машинного обучения https://machinelearningmastery.ru/smarter-ways-to-encode-categorical-data-for-machine-learning-part-1-of-3-6dca2f71b159/
# * Статья про "непонятную" метрику ROC-AUC https://dyakonov.org/2017/07/28/auc-roc-площадь-под-кривой-ошибок/
# * Хочешь подтянуть математику для DS?) https://academy.stepik.org/math-for-data-science
# * Результаты обучения моделей можно визуализировать 😎 https://www.datatechnotes.com/2019/08/elasticnet-regression-example-in-python.html
# * В нашем деле нужно быть всегда в курсе всех новинок, новостей и тд, вот тут публикуют новости в области DS: https://www.infoq.com/data-analysis/news/
# * Всем аналитикам данных рекомендую книгу Даниела Канемана "Думай медленно, решай быстро"
