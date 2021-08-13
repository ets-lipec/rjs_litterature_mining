# README

wordanalysis package contains all the functions used in the main code. The main code is also use as a test file this is why it is in the package folder : [main_word_analysis.py](https://github.com/ets-lipec/rjs_litterature_mining/blob/convertopackage/WordAnalysis/main_words_analysis.py)


## Requirements

To use wordanalysis package, you need to install, if it's not already done, all the others package use inside it. To do so, you need to write the following command in your prompt command window (ex : Anaconda Prompt) :

```linux
pip install -r requirements.txt
```


## How to install the package
### With prompt command
1. You need to download wordanalysis_package folder. 
    1. Press on the green button Code (On the [main page](https://github.com/ets-lipec/rjs_litterature_mining))
    1. Choose Download ZIP
    1. Save it where you want
    1. Extract the ZIP file
    1. Keep only the wordanalysis_package (delete the rest) because the rest takes memories on your computer for nothing
1. Open your prompt and :
    1. Change directory to wordanalysis_package
        ```linux
        cd yourPath
        ```
        Example :

        >cd C:\Users\robert\Desktop\S3\Modelisation\rjs_litterature_mining\WordAnalysis\wordanalysis_package
    1. Install the wordanalysis package by using his dynamic setup file
        ```linux
        python setup.py install
        ```
    1. Open Python
        ```linux
        python
        ```
    1. Import in your python the package
        ```linux
        import wordanalysis
        ```
    1. Exit Python
        ```linux
        exit()
        ```
1. Close your prompt
1. Then you just need to import the package in the beginning of your code as per example :
    ```linux
    import wordanalysis as wa
    ```


## Class and methods

* Process :
    * nb_art_vs_2sub(word1, word2, df, col_words)
    * article_with_word(word, df, col_word, col_info, col_ID)
    * most_common_bigrams(df, col_text, top_x)
    * most_common_trigrams(df, col_text, top_x)
    * plot_word_by_year(word, df, col_word, col_year, path)
    * nb_pub_by_year(df, col_year, path_svg)
    * map_publisher_city(df, col_city, path)
    * score(df, lst_word=None, lst_score=None, col_word=None, limit=None, col_num=None, condition='<')

* RawDf :
    * preprocess()

* RawTxt :
    * preprocess(stopwords_file, opt_caps='no', opt_stem='no')

* WOSdf

For more informations about those functions see there heading directly in [wordanalysis_package.py](https://github.com/jaklengaigne/rjs_litterature_mining/blob/main/WordAnalysis/wordanalysis/wordanalysis.py)