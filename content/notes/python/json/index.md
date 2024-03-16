---
title: Python Json
weight: 210
menu:
  notes:
    name: Json
    identifier: notes-python-json
    parent: notes-python
    weight: 20
---

<!-- Variable -->
{{< note title="Json Normalize" >}}

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