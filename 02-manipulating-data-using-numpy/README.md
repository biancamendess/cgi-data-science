# NumPy

Material de estudo da primeira aula de **NumPy** do Matsuo Lab 2026.

## Sobre

Nesta aula, foi apresentada a biblioteca **NumPy**, utilizada principalmente para computação numérica e manipulação eficiente de arrays em Python.

O foco inicial foi entender a estrutura `ndarray`, suas principais características e como trabalhar com dados numéricos de forma mais eficiente.

## Conteúdos estudados

* O que é NumPy
* `ndarray`
* Criação de arrays
* `shape`
* `ndim`
* `size`
* `dtype`
* Indexação
* Slicing
* Alteração de valores
* Operações aritméticas
* Agregações
* `axis`

## 1. O que é NumPy?

**NumPy** é uma biblioteca Python voltada para computação numérica.

Seu principal objeto é o `ndarray` (N-dimensional array), uma estrutura utilizada para armazenar e manipular conjuntos de dados de forma eficiente.

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
```

## 2. `ndarray`

Um `ndarray` é um array multidimensional do NumPy.

```python
array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Esse array possui:

* 2 dimensões
* 2 linhas
* 3 colunas
* 6 elementos

## 3. Principais atributos

### `shape`

Indica o tamanho de cada dimensão do array.

```python
array.shape
```

Resultado:

```text
(2, 3)
```

Neste caso, o array possui **2 linhas e 3 colunas**.

### `ndim`

Indica a quantidade de dimensões.

```python
array.ndim
```

Resultado:

```text
2
```

### `size`

Indica a quantidade total de elementos.

```python
array.size
```

Resultado:

```text
6
```

### `dtype`

Indica o tipo de dado armazenado.

```python
array.dtype
```

Exemplo:

```text
int64
```

## 4. Indexação

A indexação permite acessar elementos específicos do array.

```python
array[0]
```

Acessando um elemento específico:

```python
array[0, 1]
```

Como no Python, a indexação começa em `0`.

## 5. Slicing

O slicing permite selecionar uma parte do array.

```python
array[0:2]
```

Também é possível selecionar partes específicas de arrays multidimensionais:

```python
array[:, 1]
```

Nesse exemplo:

* `:` seleciona todas as linhas
* `1` seleciona a segunda coluna

## 6. Alteração de valores

Os valores de um array podem ser modificados diretamente por meio da indexação.

```python
array[0, 0] = 10
```

Agora o primeiro elemento do array passa a ser `10`.

## 7. Operações aritméticas

O NumPy permite realizar operações diretamente sobre arrays.

```python
array = np.array([1, 2, 3])

array + 10
```

Resultado:

```text
[11 12 13]
```

Também é possível realizar operações entre arrays:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b
```

Resultado:

```text
[5 7 9]
```

## 8. Agregações

Funções de agregação permitem obter informações resumidas dos valores de um array.

```python
array.sum()
array.mean()
array.min()
array.max()
```

Exemplo:

```python
array = np.array([1, 2, 3, 4, 5])

array.sum()
```

Resultado:

```text
15
```

## 9. `axis`

O parâmetro `axis` permite indicar **em qual dimensão uma operação deve ser realizada**.

Exemplo:

```python
array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Somando por coluna:

```python
array.sum(axis=0)
```

Resultado:

```text
[5 7 9]
```

Somando por linha:

```python
array.sum(axis=1)
```

Resultado:

```text
[ 6 15]
```

## Conclusão

A primeira aula serviu como introdução à estrutura e ao funcionamento dos arrays do NumPy.

Os principais conceitos estudados foram `ndarray`, dimensões, indexação, slicing, operações, agregações e `axis`. Esses conceitos formam a base para trabalhar posteriormente com bibliotecas como **Pandas**, além de serem importantes para tarefas de Ciência de Dados e Machine Learning.

## Referências

* [NumPy Documentation](https://numpy.org/doc/)
* Matsuo Lab — Data Science Course 2026

## Homework

### Homework 1 - Efficient Data Manipulation Using NumPy

Primeiro exercício prático da formação, com foco em manipulação eficiente de dados utilizando NumPy.

- [Enunciado](./question1.md)
- [Minha solução](./HW1.py)