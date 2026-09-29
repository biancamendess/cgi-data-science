## Questão

Implementar uma função que recebe um array 1D do NumPy contendo números inteiros e retorna apenas os elementos que são **múltiplos de 5 e ímpares**.

### Entrada

```python
homework(a: np.ndarray) -> np.ndarray
```

`a` é um array 1D de inteiros.

### Saída

Um array NumPy contendo os elementos que atendem às duas condições:

* São múltiplos de 5;
* São números ímpares.

### Exemplo

```python
a = np.array([1, 5, 10, 3, 4, 25, 30])

result = homework(a)

print(result)
```

Resultado:

```text
[5 25]
```

### Testes

Também foram fornecidos casos adicionais para verificar a solução, incluindo:

* Um array diferente com múltiplos de 5 e ímpares;
* Um array sem nenhum elemento que atenda às condições;
* Casos com valores negativos no processo de avaliação.

### Regras

* Manter o nome e os parâmetros da função `homework()`;
* Implementar a solução dentro da própria função;
* Não utilizar `import` dentro da função;
* Retornar um array NumPy;
* Submeter a função completa no Omnicampus.

### Submissão

A função completa deve ser copiada para o Omnicampus. O sistema utiliza casos adicionais que não aparecem no notebook para avaliar a solução.

A atividade vale **3 pontos** quando submetida corretamente dentro do prazo. Em caso de submissão após o prazo, a pontuação máxima é **2 pontos**.




