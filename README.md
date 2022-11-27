```
pip install fastapi
pip install "uvicorn[standard]"
uvicorn main:app --reload --host 0.0.0.0
```


```
pip freeze | xargs pip uninstall -y
```