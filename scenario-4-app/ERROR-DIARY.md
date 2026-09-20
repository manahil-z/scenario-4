# ERROR-DIARY.md — Scenario 4: Deployment

## Error 1: `streamlit` command not recognized

**Error:** `streamlit : The term 'streamlit' is not recognized as the name of a cmdlet, function, script file, or operable program.`

**My diagnosis:** I thought Streamlit wasn't installed at all.

**AI's diagnosis:** The AI suggested it could be an installation issue or a PATH issue, and recommended running the app through Python directly (`python -m streamlit run app.py`) to bypass PATH problems.

**Root cause:** `pip install streamlit` needed to be run first — the package wasn't installed yet. Even after installing, `python -m streamlit` was the more reliable way to run it since the `streamlit` command itself wasn't recognized directly in my terminal's PATH.

---

## Error 2: `ModuleNotFoundError: No module named 'joblib'`

**Error:** App failed to load with a missing module error for `joblib`.

**My diagnosis:** Assumed all necessary packages were already installed since the notebook worked.

**AI's diagnosis:** Explained that notebook and terminal environments can have different installed packages, and that `joblib` needed to be installed separately in the environment running the Streamlit app.

**Root cause:** `joblib` was available in my Jupyter/notebook environment but not in the terminal environment used to run the Streamlit app. Fixed with `pip install joblib`.

---

## Error 3: `ModuleNotFoundError: No module named 'sklearn'`

**Error:** Same pattern as Error 2, but for scikit-learn.

**My diagnosis:** Confused at first since `app.py` doesn't explicitly `import sklearn`.

**AI's diagnosis:** Explained that loading a saved model with `joblib.load()` requires the library that built the model (scikit-learn) to be installed, even if `app.py` doesn't import it directly, since the object internally depends on sklearn classes.

**Root cause:** Missing `scikit-learn` install in the terminal environment. Fixed with `pip install scikit-learn`.

---

## Error 4: `ModuleNotFoundError: No module named '_loss'`

**Error:** Model failed to load with an internal module error.

**My diagnosis:** Unclear at first — assumed the model file itself was corrupted.

**AI's diagnosis:** Identified this as a scikit-learn version mismatch between the environment that trained/saved the model and the environment loading it, since internal modules can change between versions.

**Root cause:** Notebook used scikit-learn 1.7.2, but the terminal environment had 1.9.1 installed. Fixed by installing the matching version: `pip install scikit-learn==1.7.2`.

---

## Error 5: `NameError: name 'gender' is not defined`

**Error:** App crashed when trying to build the input DataFrame, referencing an undefined variable `gender`.

**My diagnosis:** Went back through the input section of `app.py` and found that the `gender` selectbox line had been left out when building the form, even though it was used later in the prediction dictionary.

**AI's diagnosis:** Same — pointed directly to the missing `st.selectbox` line for `gender`.

**Root cause:** A variable was referenced before being defined. Fixed by adding `gender = st.selectbox("Gender", ["Female", "Male"])` before the prediction section.