import sys
import base64
import os
import json
import flask
from flask import request, send_from_directory, send_file
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/Algorithm', methods=['POST', "PUT", "GET", "DELETE"])
def Algo():
    if request.method == "GET":
        var1 = request.args.get('AlgoNum')
        var2 = request.args.get('FileNum')
        FileDir = "./Algorithms-InputFiles/"+var1+"_input/"+var1+"-"+var2+".json"
        json_file = open(FileDir)
        variables = json.load(json_file)
        var1 = int(var1)
        if var1 == 0:
            m = len(variables["data"][0])
            print("Length of String 1 is " + str(m))
            n = len(variables["data"][1])
            value =  lcs(variables["data"][0],variables["data"][1],m,n)
            print("Answer is: " + value)
            response = flask.jsonify(answer = value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 1:
            m = len(variables["data"][0])
            n = len(variables["data"][1])
            value = shortestSuperSequence(variables["data"][0], variables["data"][1])
            response = flask.jsonify(answer = value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 3:
            m = len(variables["data"][0])
            print(m)
            n = len(variables["data"][1])
            value = editDistance(
                variables["data"][0], variables["data"][1])
            print(value)
            response = flask.jsonify(answer=value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 2:
            value = LIS(variables["data"])
            response = flask.jsonify(answer=value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 4:
            m = len(variables["data"])
            dims = variables["data"]
            T = [[0 for x in range(len(dims))] for y in range(len(dims))]
            value = MatrixChainMultiplication(variables["data"], 0, m-1, T)
            print(value)
            response = flask.jsonify(answer=value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 5:
            n = len(variables["data"]["v"])
            lookup = {}
            value = knapSack(variables["data"]["v"], variables["data"]["w"], n-1, variables["data"]["W"], lookup)
            response = flask.jsonify(answer=value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 6:
            value = partition(variables["data"])
            print(value)
            response = flask.jsonify(answer=str(value))
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 7:
            value = rodCut(variables["data"]["p"], variables["data"]["n"])
            response = flask.jsonify(answer=value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response 
        elif var1 == 8:
            value = findMinCoins(variables["data"]["coins"], variables["data"]["money"])
            print(value)
            response = flask.jsonify(answer=value)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        elif var1 == 9:
            lookup = [-1] * (len(variables["data"]["s"]) + 1)
            value = wordBreak(variables["data"]["wordDict"], variables["data"]["s"],lookup)
            print(value)
            response = flask.jsonify(answer=str(value))
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response

def lcs(X, Y, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]
    lcs = [""] * (index+1)
    lcs[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    print("LCS of " + X + " and " + Y + " is " + "".join(lcs))
    merge = "".join(lcs)
    return merge

def shortestSuperSequence(a, b):
    m = len(a)
    n = len(b)
    func = lcs(a, b, m, n)
    scs = ""
    # Consume lcs
    while len(func) > 0:
        if a[0] == func[0] and b[0] == func[0]:
            # Part of the func, so consume from all strings
            scs += func[0]
            func = func[1:]
            a = a[1:]
            b = b[1:]
        elif a[0] == func[0]:
            scs += b[0]
            b = b[1:]
        else:
            scs += a[0]
            a = a[1:]
    # append remaining characters
    return scs + a + b

def editDistance(X, Y):

    (m, n) = (len(X), len(Y))

    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(1, m + 1):
        T[i][0] = i                     # (case 1)

    for j in range(1, n + 1):
        T[0][j] = j                     # (case 1)

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):

        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:    # (case 2)
                cost = 0                # (case 2)
            else:
                cost = 1                # (case 3c)

            T[i][j] = min(T[i - 1][j] + 1,          # deletion (case 3b)
                          T[i][j - 1] + 1,          # insertion (case 3a)
                          T[i - 1][j - 1] + cost)   # replace (case 2 + 3c)

    return T[m][n]

def LIS(A):

    # list to store sub-problem solution. L[i] stores the length
    # of the longest increasing sub-sequence ends with A[i]
    L = [0] * len(A)

    # longest increasing sub-sequence ending with A[0] has length 1
    L[0] = 1

    # start from second element in the list
    for i in range(1, len(A)):
        # do for each element in sublist A[0..i-1]
        for j in range(i):
            # find longest increasing sub-sequence that ends with A[j]
            # where A[j] is less than the current element A[i]
            if A[j] < A[i] and L[j] > L[i]:
                L[i] = L[j]

        # include A[i] in LIS
        L[i] = L[i] + 1

    # return longest increasing sub-sequence (having maximum length)
    return max(L)

def MatrixChainMultiplication(dims, i, j, T):

    if j <= i + 1:
        return 0

    min = float('inf')

    if T[i][j] == 0:

        for k in range(i + 1, j):

            cost = MatrixChainMultiplication(dims, i, k, T)

            cost += MatrixChainMultiplication(dims, k, j, T)

            cost += dims[i] * dims[k] * dims[j]

            if cost < min:
                min = cost

        T[i][j] = min

    return T[i][j]

def knapSack(v, w, n, W, lookup):

    if W < 0:
        return float('-inf')

    if n < 0 or W == 0:
        return 0

    key = (n, W)

    if key not in lookup:

        include = v[n] + knapSack(v, w, n - 1, W - w[n], lookup)

        exclude = knapSack(v, w, n - 1, W, lookup)

        lookup[key] = max(include, exclude)

    return lookup[key]

def subsetSum(A, n, sum):
    T = [[False for x in range(sum + 1)] for y in range(n + 1)]
    for i in range(n + 1):
        T[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]
    return T[n][sum]

def partition(A):
    total = sum(A)
    return (total & 1) == 0 and subsetSum(A, len(A), total // 2)

def rodCut(price, n):
    T = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            T[i] = max(T[i], price[j - 1] + T[i - j])
    return T[n]

def findMinCoins(S, N):
    T = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i] = float('inf')
        for c in range(len(S)):
            if i - S[c] >= 0:
                res = T[i - S[c]]
                if res != float('inf'):
                    T[i] = min(T[i], res + 1)
    if T[N] == float('inf'):
        T[N] = 0
    return T[N]

def wordBreak(dict, str, lookup):
    n = len(str)
    if n == 0:
        return True
    if lookup[n] == -1:
        lookup[n] = 0
        for i in range(1, n + 1):
            prefix = str[:i]
            if prefix in dict and wordBreak(dict, str[i:], lookup):
                lookup[n] = 1
                return True
    return lookup[n] == 1

app.run(host="localhost")
