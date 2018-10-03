def compute_score(y, y_hat):  # to be minimized
    assert len(y) == len(y_hat)
    return -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))


def predict_baseline(X_train, y_train, X_test):
    return np.array([y_train.mean()] * len(X_test))


def full_cv(predict_func, X, y, folds=10, shuffle=True, verbose=True):
    y = np.array(y)
    index_shuf = np.array(range(len(X)))
    if shuffle:
        random.shuffle(index_shuf)

    X_folds = np.array_split(index_shuf, folds)
    y_folds = np.array_split(index_shuf, folds)
    y_predict = np.array([])
    for k in range(folds):
        if verbose:
            print('\r{:7.5}%  '.format(k * 100.0 / folds))
        # We use 'list' to copy, in order to 'pop' later on
        X_train = list(X_folds)
        X_test = X_train.pop(k)
        X_train = np.concatenate(X_train)
        y_train = reshape_y_train(k, y_folds)
        new_y_hat = predict_func(X.ix[X_train], y[y_train], X.ix[X_test])
        y_predict = np.concatenate([y_predict, new_y_hat])
    return compute_score(y[index_shuf], y_predict)


def reshape_y_train(k, y_folds):
    y_train = list(y_folds)
    y_train.pop(k)
    y_train = np.concatenate(y_train)
    return y_train


baseline_score = full_cv(predict_baseline, adult, adult.y, verbose=False)
print('baseline_score=', baseline_score)  # 0.568739686466 (10 folds)
# baseline_score = compute_score(adult.income, np.array([adult.income.mean()]*len(adult.income))) # 0.5520112931
