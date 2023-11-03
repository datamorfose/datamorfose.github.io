---
title: Python Variables
weight: 210
menu:
  notes:
    name: Variables
    identifier: notes-python-variables
    parent: notes-python
    weight: 10
---

<!-- Variable -->
{{< note title="Variable" >}}

```python
NAME="John"
echo $NAME
echo "$NAME"
echo "${NAME}
```

{{< /note >}}

<!-- Condition -->
{{< note title="Condition" >}}

```python
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
fi
```

{{< /note >}}


<!-- Teste -->
{{< note title="Teste" >}}

```python
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
fi
teste
```

{{< /note >}}