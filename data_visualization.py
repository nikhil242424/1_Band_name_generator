{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.3"
    },
    "colab": {
      "provenance": [],
      "collapsed_sections": [
        "u5KcSXt1Gxuk",
        "arguGp3ZGxu1"
      ],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nikhil242424/1_Band_name_generator/blob/master/data_visualization.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MAAKxOwsGxuj"
      },
      "source": [
        "## Get the Data\n",
        "\n",
        "Either use the provided .csv file or (optionally) get fresh (the freshest?) data from running an SQL query on StackExchange:\n",
        "\n",
        "Follow this link to run the query from [StackExchange](https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com) to get your own .csv file\n",
        "\n",
        "<code>\n",
        "select dateadd(month, datediff(month, 0, q.CreationDate), 0) m, TagName, count(*)\n",
        "from PostTags pt\n",
        "join Posts q on q.Id=pt.PostId\n",
        "join Tags t on t.Id=pt.TagId\n",
        "where TagName in ('java','c','c++','python','c#','javascript','assembly','php','perl','ruby','visual basic','swift','r','object-c','scratch','go','swift','delphi')\n",
        "and q.CreationDate < dateadd(month, datediff(month, 0, getdate()), 0)\n",
        "group by dateadd(month, datediff(month, 0, q.CreationDate), 0), TagName\n",
        "order by dateadd(month, datediff(month, 0, q.CreationDate), 0)\n",
        "</code>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "u5KcSXt1Gxuk"
      },
      "source": [
        "## Import Statements"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ru4Wq-pXGxuk"
      },
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": 62,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xEP6beuEGxun"
      },
      "source": [
        "## Data Exploration"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "w3Q75B4CGxun"
      },
      "source": [
        "**Challenge**: Read the .csv file and store it in a Pandas dataframe"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bm7hQtEGIiri"
      },
      "source": [
        "df = pd.read_csv('/content/QueryResults.csv',names = ['DATES' , 'TAGS' , 'POSTS'] , header=0)"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "x2WnDM75Gxup"
      },
      "source": [
        "\n",
        "\n",
        "```\n",
        "# This is formatted as code\n",
        "```\n",
        "\n",
        "**Challenge**: Examine the first 5 rows and the last 5 rows of the of the dataframe"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "50oqpUxVIiJf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "f70ba30b-72c6-4f8f-f1c4-ba1992e8d9f1"
      },
      "source": [
        "df.head()\n",
        "df.tail()\n"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    DATES   TAGS  POSTS\n",
              "1986  2020-07-01 00:00:00      r   5694\n",
              "1987  2020-07-01 00:00:00     go    743\n",
              "1988  2020-07-01 00:00:00   ruby    775\n",
              "1989  2020-07-01 00:00:00   perl    182\n",
              "1990  2020-07-01 00:00:00  swift   3607"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-eaa6723b-f334-42ed-82de-e7ae211e3a4f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>DATES</th>\n",
              "      <th>TAGS</th>\n",
              "      <th>POSTS</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1986</th>\n",
              "      <td>2020-07-01 00:00:00</td>\n",
              "      <td>r</td>\n",
              "      <td>5694</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1987</th>\n",
              "      <td>2020-07-01 00:00:00</td>\n",
              "      <td>go</td>\n",
              "      <td>743</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1988</th>\n",
              "      <td>2020-07-01 00:00:00</td>\n",
              "      <td>ruby</td>\n",
              "      <td>775</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1989</th>\n",
              "      <td>2020-07-01 00:00:00</td>\n",
              "      <td>perl</td>\n",
              "      <td>182</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1990</th>\n",
              "      <td>2020-07-01 00:00:00</td>\n",
              "      <td>swift</td>\n",
              "      <td>3607</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-eaa6723b-f334-42ed-82de-e7ae211e3a4f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-eaa6723b-f334-42ed-82de-e7ae211e3a4f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-eaa6723b-f334-42ed-82de-e7ae211e3a4f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0o9hvVgyGxus"
      },
      "source": [
        "**Challenge:** Check how many rows and how many columns there are.\n",
        "What are the dimensions of the dataframe?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZUidjCPFIho8"
      },
      "source": [
        "df.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ybZkNLmxGxuu"
      },
      "source": [
        "**Challenge**: Count the number of entries in each column of the dataframe"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Sc1dmmOoIg2g"
      },
      "source": [
        "df.count()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hlnfFsscGxuw"
      },
      "source": [
        "**Challenge**: Calculate the total number of post per language.\n",
        "Which Programming language has had the highest total number of posts of all time?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9-NYFONcIc1X"
      },
      "source": [
        "df.groupby('TAGS').sum()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iVCesB49Gxuz"
      },
      "source": [
        "Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.\n",
        "\n",
        "**Challenge**: How many months of data exist per language? Which language had the fewest months with an entry?\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hDT4JlJNJfgQ"
      },
      "source": [
        "df.groupby('TAGS').count()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "arguGp3ZGxu1"
      },
      "source": [
        "## Data Cleaning\n",
        "\n",
        "Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of \"2008-07-01 00:00:00\" to a datetime object with the format of \"2008-07-01\""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5nh5a4UtGxu1"
      },
      "source": [
        "df['DATES'].head()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "016H-Fy4Gxu3"
      },
      "source": [
        "df.DATES = pd.to_datetime(df.DATES)\n",
        "df.head()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4EiSd7pdGxu5"
      },
      "source": [
        "print(type(df.DATES[0]))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rWAV6tuzGxu6"
      },
      "source": [
        "## Data Manipulation\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aHhbulJaGxu7"
      },
      "source": [
        "reshaped_df = df.pivot(index='DATES' , columns='TAGS' , values='POSTS')"
      ],
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RWKcVIyFKwHM"
      },
      "source": [
        "**Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "v-u4FcLXGxu9"
      },
      "source": [
        "reshaped_df.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NUyBcaMMGxu-"
      },
      "source": [
        "reshaped_df.columns"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LnUIOL3LGxvA"
      },
      "source": [
        "reshaped_df.head(145)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BoDCuRU0GxvC"
      },
      "source": [
        "**Challenge**: Count the number of entries per programming language. Why might the number of entries be different?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-peEFgaMGxvE"
      },
      "source": [
        "reshaped_df.count()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "01f2BCF8GxvG"
      },
      "source": [
        "reshaped_df = reshaped_df.fillna(0)"
      ],
      "execution_count": 59,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KooRRxAdGxvI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9628055b-bb86-47b5-872c-7ac6c6a60c0c"
      },
      "source": [
        "reshaped_df.isna().values.any()"
      ],
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8xU7l_f4GxvK"
      },
      "source": [
        "## Data Visualisaton with with Matplotlib\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "njnNXTlhGxvK"
      },
      "source": [
        "**Challenge**: Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S0OS8T8iGxvL",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "outputId": "22e9a955-ef61-4939-ec42-0af74560aa69"
      },
      "source": [
        "plt.plot(reshaped_df.index, reshaped_df.python, 'bo')"
      ],
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7faf1502a7d0>]"
            ]
          },
          "metadata": {},
          "execution_count": 71
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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Ikc+IjwAQLz77rs226ZNmyaysrIcfubYsWMCgPjkk0+Ube+9957QaDTi7NmzQggh3njjDdGjRw/R0NCgxCxatEgMHDhQef/www+LzMxMm2OnpaWJn//856rPv76+XgAQ9fX1qj9DRETObdkiRGqqENKDJOmVmirEggVttxsMUrwzzc3S5zQa28/KL41G2t/62K1jDAbpWBT61P5++6SEvKysDAkJCRg4cCCefvppXJSXlgVQXl6O7t274/bbb1e2paenIyIiAgcOHFBixowZA61Wq8RkZGTgxIkT+O6775SY9PR0m+/NyMhAeXm5w/NqaGiA2Wy2eRERkffIk2ztjaYsWwb89rfuP7JRU649axab7lFbXk9y7rnnHvz5z39GSUkJfvOb32D37t2YOHEiLP/q2GQymZDQqq93p06dEBsbC5PJpMQkJibaxMjvXcXI++0pKChATEyM8jIYDJ5dLBERKVwtWgkAzz8vzdFx95GNo743ckO/m25Sdxw23etYvF5d9cgjjyj/PXToUNx666248cYbUVZWhvHjx3v769ySl5eH3Nxc5b3ZbGaiQ0TkJe5WQbnL2argZWXqjsGmex2Lz0vI+/fvj7i4OHz11VcYP348kpKSUFtbaxPT3NyMS5cuISkpCQCQlJSEmpoamxj5vasYeb89Op0OOp3O42siIqK21C7Z4MloiqNybbmCy1XTPXcX4qTQ5vNlHc6cOYOLFy8i+V/ps9FoRF1dHSoqKpSYXbt2oaWlBWlpaUrMnj170NTUpMQUFxdj4MCB6NGjhxJTUlJi813FxcUwGo2+viQiog7LumrKeu2ooiJpuQQ1fDGaonaZBVY0dTDuzmi+fPmyOHjwoDh48KAAIH7729+KgwcPim+//VZcvnxZ/PKXvxTl5eWiqqpK/OMf/xAjRowQN910k7h27ZpyjHvuuUfcdttt4sCBA+LDDz8UN910k5gyZYqyv66uTiQmJorHH39cHDlyRGzYsEFER0eL3//+90rMRx99JDp16iSWLVsmjh8/LvLz80Xnzp3F4cOHVV8Lq6uIKJw0NwtRWirEunXSX29XEjmrmnJU+eTvCid756imgotCi9rfb7eTnNLSUgGgzWvatGnihx9+EBMmTBDx8fGic+fOok+fPmLWrFnCZDLZHOPixYtiypQpomvXrkKv14vp06eLy5cv28R8/vnn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fRe7du1Cv379bPaPHDkSnTt3RklJibLtxIkTOHXqFIxGIwBpvs3hw4dRW1urxBQXF0Ov12PQoEEAgB9++AEREba3LjIyUjmHUOCNe6WG0WjEnj170NTUpGwrLi7GwIED0aNHD88vxA/8da8AqRwzMzMTv/nNb2yGhUOFv+5VeXk5KisrldfLL7+Mbt26obKyEg8++KDXrseX/HWv7rrrLjQ3N+Prr79Wtv3zn/8EAPTp08fDq/Aff90vZ/++t7S0eHAF/uOte3X06FGMGzcO06ZNs9tywGg02hwDkP59d/ffPZ8K1IxnX3j66adFTEyMKCsrE9XV1crrhx9+UGLmzJkjevfuLXbt2iU+/fRTYTQahdFoVPY3NzeLIUOGiAkTJojKykqxc+dOER8fL/Ly8pSYNWvWiE6dOok33nhDfP311+LDDz8Ut99+uxg1apRfr9cT3rhXQgjx5ZdfioMHD4qf//zn4uabbxYHDx4UBw8eVKqp6urqRGJionj88cfFkSNHxIYNG0R0dLT4/e9/79fr9YS/7tWuXbtEdHS0yMvLs/meixcv+vV6PeGve9VaKFZX+eteWSwWMWLECDFmzBjx2WefiU8//VSkpaWJn/3sZ369Xk/5636VlJQIjUYjlixZIv75z3+KiooKkZGRIfr06WPzXcHMG/fq8OHDIj4+Xjz22GM2x6itrVVivvnmGxEdHS0WLFggjh8/LlatWiUiIyPFzp07/Xq9zoRVkgPA7mvNmjVKzNWrV8UzzzwjevToIaKjo8WDDz4oqqurbY5z8uRJMXHiRBEVFSXi4uLE888/L5qammxifve734lBgwaJqKgokZycLKZOnSrOnDnjj8v0Cm/dq5/85Cd2j1NVVaXEfP755+Luu+8WOp1OpKSkiFdeecVPV+kd/rpX06ZNs7v/Jz/5if8u1kP+/P+VtVBMcvx5r86ePSuys7NF165dRWJionjyySdDKnkWwr/3a/369eK2224TN9xwg4iPjxf/9m//Jo4fP+6nK/WcN+5Vfn6+3WP06dPH5rtKS0vF8OHDhVarFf3797f5jmCgESJEnq8QERERuSGs5uQQERERyZjkEBERUVhikkNERERhiUkOERERhSUmOURERBSWmOQQERFRWGKSQ0RERGGJSQ4RERGFJSY5REREFJaY5BAREVFYYpJDREREYYlJDhEREYWl/w/fUAazC3gCawAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EU6AV1l9GxvM"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_Qzzg6b_GxvO"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Sm2DL5tZGxvQ"
      },
      "source": [
        "**Challenge**: Show two line (e.g. for Java and Python) on the same chart."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T-0vClQSGxvQ"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3jSjfPy7GxvY"
      },
      "source": [
        "# Smoothing out Time Series Data\n",
        "\n",
        "Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html)."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s3WYd3OgGxvc"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WMJOX8Y2Gxvd"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fAvvarA7Gxvf"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Gm0Ww0S4Gxvg"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    }
  ]
}