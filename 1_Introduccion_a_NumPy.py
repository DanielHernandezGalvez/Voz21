{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a href=\"https://colab.research.google.com/drive/1gmnUN5sqWh7SgP3PJgpU1S5eP-Vr_wvT\">Abre este Jupyter en Google Colab</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introducción a NumPy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Numpy](https://numpy.org) es una librería fundamental para la computación científica con Python.\n",
    "* Proporciona arrays N-dimensionales\n",
    "* Implementa funciones matemáticas sofisticadas\n",
    "* Proporciona herramientas para integrar C/C++ y Fortran\n",
    "* Proporciona mecanismos para facilitar la realización de tareas relacionadas con álgebra lineal o números aleatorios"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ]
    }
   ],
   "source": [
    "# Instalación de Numpy y Matplotlib\n",
    "!pip install numpy\n",
    "!pip install matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Arrays"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Un **array** es una estructura de datos que consiste en una colección de elementos (valores o variables), cada uno identificado por al menos un índice o clave. Un array se almacena de modo que la posición de cada elemento se pueda calcular a partir de su tupla de índice mediante una fórmula matemática. El tipo más simple de array es un array lineal, también llamado array unidimensional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En numpy:\n",
    "* Cada dimensión se denomina **axis**\n",
    "* El número de dimensiones se denomina **rank**\n",
    "* La lista de dimensiones con su correspondiente longitud se denomina **shape**\n",
    "* El número total de elementos (multiplicación de la longitud de las dimensiones) se denomina **size**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Array cuyos valores son todos 0\n",
    "a = np.zeros((2, 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., 0.],\n",
       "       [0., 0., 0., 0.]])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_**a**_ es un array:\n",
    "* Con dos **axis**, el primero de longitud 2 y el segundo de longitud 4\n",
    "* Con un **rank** igual a 2\n",
    "* Con un **shape** igual (2, 4)\n",
    "* Con un **size** igual a 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 4)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Creación de Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.]],\n",
       "\n",
       "       [[0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.]]])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Array cuyos valores son todos 0\n",
    "np.zeros((2, 3, 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1., 1., 1., 1.],\n",
       "        [1., 1., 1., 1.],\n",
       "        [1., 1., 1., 1.]],\n",
       "\n",
       "       [[1., 1., 1., 1.],\n",
       "        [1., 1., 1., 1.],\n",
       "        [1., 1., 1., 1.]]])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Array cuyos valores son todos 1\n",
    "np.ones((2, 3, 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[8, 8, 8, 8],\n",
       "        [8, 8, 8, 8],\n",
       "        [8, 8, 8, 8]],\n",
       "\n",
       "       [[8, 8, 8, 8],\n",
       "        [8, 8, 8, 8],\n",
       "        [8, 8, 8, 8]]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Array cuyos valores son todos el valor indicado como segundo parámetro de la función\n",
    "np.full((2, 3, 4), 8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1.21533711e-311, 1.21531025e-311, 2.05833592e-312,\n",
       "         6.79038654e-313, 2.48273508e-312, 2.35541533e-312,\n",
       "         6.79038654e-313, 2.05833592e-312, 2.35541533e-312],\n",
       "        [2.14321575e-312, 6.79038654e-313, 2.35541533e-312,\n",
       "         6.79038654e-313, 2.35541533e-312, 2.35541533e-312,\n",
       "         6.79038654e-313, 2.29175545e-312, 2.50395503e-312],\n",
       "        [2.29175545e-312, 2.41907520e-312, 2.22809558e-312,\n",
       "         2.12199579e-312, 2.10077583e-312, 2.12199579e-312,\n",
       "         6.79038654e-313, 2.35541533e-312, 2.35541533e-312]],\n",
       "\n",
       "       [[2.44029516e-312, 2.18565567e-312, 2.33419537e-312,\n",
       "         2.35541533e-312, 2.37663529e-312, 2.41907520e-312,\n",
       "         2.31297541e-312, 2.46151512e-312, 2.35541533e-312],\n",
       "        [2.12199579e-312, 6.79038654e-313, 2.05833592e-312,\n",
       "         2.16443571e-312, 2.33419537e-312, 2.22809558e-312,\n",
       "         2.33419537e-312, 2.33419537e-312, 9.76118064e-313],\n",
       "        [2.48273508e-312, 2.29175545e-312, 8.48798317e-313,\n",
       "         9.33678148e-313, 1.08221785e-312, 6.79038653e-313,\n",
       "         8.70018275e-313, 6.79038653e-313, 8.70018275e-313]]])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# El resultado de np.empty no es predecible \n",
    "# Inicializa los valores del array con lo que haya en memoria en ese momento\n",
    "np.empty((2, 3, 9))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Inicializacion del array utilizando un array de Python\n",
    "b = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.         0.66666667 1.33333333 2.         2.66666667 3.33333333\n",
      " 4.         4.66666667 5.33333333 6.        ]\n"
     ]
    }
   ],
   "source": [
    "# Creación del array utilizando una función basada en rangos\n",
    "# (minimo, maximo, número elementos del array)\n",
    "print(np.linspace(0, 6, 10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0.4803661 , 0.04791604, 0.6585326 , 0.26318487],\n",
       "        [0.49215558, 0.91367386, 0.4091404 , 0.50591823],\n",
       "        [0.16773816, 0.60664607, 0.34644378, 0.46572176]],\n",
       "\n",
       "       [[0.4716299 , 0.92467181, 0.2884385 , 0.80479927],\n",
       "        [0.92523426, 0.64093541, 0.84163116, 0.37160562],\n",
       "        [0.12448548, 0.93544157, 0.25712712, 0.20475179]]])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Inicialización del array con valores aleatorios\n",
    "np.random.rand(2, 3, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.43861388, -1.2510498 ,  0.68775812,  0.60112712],\n",
       "       [ 0.37631383, -0.24095791, -0.0918386 ,  0.64442362]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Inicialización del array con valores aleatorios conforme a una distribución normal\n",
    "np.random.randn(2, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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quuuu07r1q1T7969G3pKAADAQA7LsqxAdyJQvF6vIiIiVFVVpfDw8EB3BwhKwXh3Vfm8lEB3AcDPcLGf33x3FQAAMBIhBwAAGImQAwAAjETIAQAARvLriscAzBWME44BNC+M5AAAACMRcgAAgJG4XAWg2TnzUhtr5gDmYiQHAAAYiZADAACMxOUqAA3CXVUAggUjOQAAwEiEHADNWtdZGxidAgxFyAEAAEYi5AAAACMRcgAAgJEIOQAAwEjcQg7gojA5F0CwYSQHAAAYiZADAACMRMgBAABGIuQAAAAjEXIAAICRCDkAIL7eATARIQcAABiJkAMAAIxEyAEAAEZixWMA58UcFQDBjJEcADgDE5ABcxByAACAkQg5AADASIQcAABgJCYeAzgLc1IAmICRHAAAYKQGh5zCwkLddtttiomJkcPh0Lp163za7733XjkcDp9txIgRPjXfffedxo0bp/DwcLVp00ZpaWk6fvy4T83evXt16623KiwsTLGxsZo/f/5ZfVm7dq169OihsLAwxcfH66233mro6QAAAEM1OOScOHFCffv21bJly85bM2LECB0+fNje/uu//sunfdy4cdq/f7/y8/O1fv16FRYWatKkSXa71+tVcnKyunTpouLiYi1YsEDZ2dl69tln7Zpt27ZpzJgxSktL0/vvv6/U1FSlpqZq3759DT0lAABgIIdlWdYlP9nh0Ouvv67U1FR737333qujR4+eNcJT7+OPP1avXr20a9cuDRo0SJKUl5enUaNG6YsvvlBMTIyWL1+uP/3pT/J4PHI6nZKkWbNmad26dSotLZUk3XnnnTpx4oTWr19vH/vGG29Uv379tGLFiovqv9frVUREhKqqqhQeHn4J7wBgJubkSOXzUgLdBQDncbGf336Zk7NlyxZFRkaqe/fuevDBB/Xtt9/abUVFRWrTpo0dcCQpKSlJISEh2rFjh10zZMgQO+BIktvtVllZmb7//nu7Jikpyed13W63ioqKztuv6upqeb1enw0AAJip0UPOiBEj9B//8R8qKCjQv//7v2vr1q0aOXKkamtrJUkej0eRkZE+z7niiivUrl07eTweuyYqKsqnpv7xT9XUt59LTk6OIiIi7C02NvbnnSwAAGiyGv0W8rvuusv+OT4+Xn369FG3bt20ZcsWDR8+vLFfrkGysrKUmZlpP/Z6vQQdAAAM5fd1cq655hp16NBBBw4c0PDhwxUdHa0jR4741Jw+fVrfffedoqOjJUnR0dGqrKz0qal//FM19e3n4nK55HK5fvY5ATDfmfOSmJ8DBCe/r5PzxRdf6Ntvv1WnTp0kSYmJiTp69KiKi4vtms2bN6uurk4JCQl2TWFhoU6dOmXX5Ofnq3v37mrbtq1dU1BQ4PNa+fn5SkxM9PcpAQCAINDgkHP8+HGVlJSopKREknTw4EGVlJSooqJCx48f1/Tp07V9+3aVl5eroKBAv/nNb3TttdfK7XZLknr27KkRI0Zo4sSJ2rlzp9577z1lZGTorrvuUkxMjCRp7NixcjqdSktL0/79+7VmzRotWbLE51LTQw89pLy8PC1cuFClpaXKzs7W7t27lZGR0QhvC9A88Q3cAEzS4JCze/du9e/fX/3795ckZWZmqn///po9e7ZCQ0O1d+9e/frXv9YvfvELpaWlaeDAgfrHP/7hc5lo5cqV6tGjh4YPH65Ro0bplltu8VkDJyIiQhs3btTBgwc1cOBAPfzww5o9e7bPWjo33XSTVq1apWeffVZ9+/bVq6++qnXr1ql3794/5/0AAACG+Fnr5AQ71skBfDGKc27MyQGaloCukwMAABBohBwAAGAkQg4AADASIQcAABiJkAMAAIxEyAEAAEby+9c6AGjauG0cgKkYyQEAAEYi5AAAACMRcgDgJ/CdXkBwIuQAAAAjEXIAAICRCDkAAMBIhBwAAGAkQg4AADASIQcAABiJkAMAF4lbyYHgwtc6AM0UH9YATMdIDgAAMBIhBwAAGImQAwAAjETIAQAARiLkAEADcZcVEBwIOQAAwEjcQg40M4xAAGguGMkBAABGIuQAAAAjEXIAAICRCDkAAMBIhBwAAGAkQg4AADASIQcAABiJkAMAAIxEyAEAAEYi5AAAACM1OOQUFhbqtttuU0xMjBwOh9atW2e3nTp1SjNnzlR8fLxatWqlmJgYjR8/Xl999ZXPMbp27SqHw+GzzZs3z6dm7969uvXWWxUWFqbY2FjNnz//rL6sXbtWPXr0UFhYmOLj4/XWW2819HQAAIChGhxyTpw4ob59+2rZsmVntf3www/as2eP/u3f/k179uzRa6+9prKyMv36178+q/aJJ57Q4cOH7W3KlCl2m9frVXJysrp06aLi4mItWLBA2dnZevbZZ+2abdu2acyYMUpLS9P777+v1NRUpaamat++fQ09JQAAYKAGf0HnyJEjNXLkyHO2RUREKD8/32ff0qVLNXjwYFVUVKhz5872/tatWys6Ovqcx1m5cqVqamr0wgsvyOl06vrrr1dJSYmeeuopTZo0SZK0ZMkSjRgxQtOnT5ckzZ07V/n5+Vq6dKlWrFjR0NMCAACG8fucnKqqKjkcDrVp08Zn/7x589S+fXv1799fCxYs0OnTp+22oqIiDRkyRE6n097ndrtVVlam77//3q5JSkryOabb7VZRUdF5+1JdXS2v1+uzAc1F11kb+AZyAM1Kg0dyGuLHH3/UzJkzNWbMGIWHh9v7//jHP2rAgAFq166dtm3bpqysLB0+fFhPPfWUJMnj8SguLs7nWFFRUXZb27Zt5fF47H1n1ng8nvP2JycnR3PmzGms0wMAAE2Y30LOqVOn9Lvf/U6WZWn58uU+bZmZmfbPffr0kdPp1O9//3vl5OTI5XL5q0vKysryeW2v16vY2Fi/vR4As505MlY+LyWAPQFwLn4JOfUB5/PPP9fmzZt9RnHOJSEhQadPn1Z5ebm6d++u6OhoVVZW+tTUP66fx3O+mvPN85Ekl8vl1xAFAACajkafk1MfcD755BNt2rRJ7du3/8nnlJSUKCQkRJGRkZKkxMREFRYW6tSpU3ZNfn6+unfvrrZt29o1BQUFPsfJz89XYmJiI54NAAAIVg0eyTl+/LgOHDhgPz548KBKSkrUrl07derUSf/6r/+qPXv2aP369aqtrbXnyLRr105Op1NFRUXasWOHhg0bptatW6uoqEjTpk3T3XffbQeYsWPHas6cOUpLS9PMmTO1b98+LVmyRIsWLbJf96GHHtIvf/lLLVy4UCkpKVq9erV2797tc5s5AABovhyWZVkNecKWLVs0bNiws/ZPmDBB2dnZZ00YrvfOO+9o6NCh2rNnj/7whz+otLRU1dXViouL0z333KPMzEyfS0l79+5Venq6du3apQ4dOmjKlCmaOXOmzzHXrl2rxx57TOXl5bruuus0f/58jRo16qLPxev1KiIiQlVVVT95SQ0IdtxZ5V/MyQEun4v9/G5wyDEJIQfNCSHHvwg5wOVzsZ/ffr2FHEBgEWwANGd8QScANAIWWwSaHkIOAAAwEiEHAAAYiZADAACMRMgBAABGIuQAAAAjEXIAAICRWCcHMBC3MgMAIzkAAMBQhBwAAGAkQg4AADASIQcAABiJkAMAAIxEyAGARsQXdQJNByEHAAAYiZADAACMRMgBAABGIuQAAAAjEXIAAICRCDkAAMBIhBwAAGAkQg4AADDSFYHuAIDGwyJ0TUf9/4vyeSkB7gnQfDGSAwAAjETIAQAARiLkAAAAIxFyAACAkQg5AADASIQcAABgJEIOAAAwEiEHAAAYicUAAQOwCGDTdeb/GxYGBC4vRnIAAICRCDkAAMBIDQ45hYWFuu222xQTEyOHw6F169b5tFuWpdmzZ6tTp05q0aKFkpKS9Mknn/jUfPfddxo3bpzCw8PVpk0bpaWl6fjx4z41e/fu1a233qqwsDDFxsZq/vz5Z/Vl7dq16tGjh8LCwhQfH6+33nqroacDAAAM1eCQc+LECfXt21fLli07Z/v8+fP117/+VStWrNCOHTvUqlUrud1u/fjjj3bNuHHjtH//fuXn52v9+vUqLCzUpEmT7Hav16vk5GR16dJFxcXFWrBggbKzs/Xss8/aNdu2bdOYMWOUlpam999/X6mpqUpNTdW+ffsaekoAAMBADsuyrEt+ssOh119/XampqZL+dxQnJiZGDz/8sB555BFJUlVVlaKiopSbm6u77rpLH3/8sXr16qVdu3Zp0KBBkqS8vDyNGjVKX3zxhWJiYrR8+XL96U9/ksfjkdPplCTNmjVL69atU2lpqSTpzjvv1IkTJ7R+/Xq7PzfeeKP69eunFStWXFT/vV6vIiIiVFVVpfDw8Et9G4CAY+JxcGDiMdA4Lvbzu1Hn5Bw8eFAej0dJSUn2voiICCUkJKioqEiSVFRUpDZt2tgBR5KSkpIUEhKiHTt22DVDhgyxA44kud1ulZWV6fvvv7drznyd+pr61zmX6upqeb1enw0AAJipUW8h93g8kqSoqCif/VFRUXabx+NRZGSkbyeuuELt2rXzqYmLizvrGPVtbdu2lcfjueDrnEtOTo7mzJlzCWcGND2M3gDAhTWru6uysrJUVVVlb4cOHQp0lwA0I11nbSCcApdRo4ac6OhoSVJlZaXP/srKSrstOjpaR44c8Wk/ffq0vvvuO5+acx3jzNc4X019+7m4XC6Fh4f7bAAAwEyNGnLi4uIUHR2tgoICe5/X69WOHTuUmJgoSUpMTNTRo0dVXFxs12zevFl1dXVKSEiwawoLC3Xq1Cm7Jj8/X927d1fbtm3tmjNfp76m/nUAAEDz1uCQc/z4cZWUlKikpETS/042LikpUUVFhRwOh6ZOnao///nP+vvf/64PP/xQ48ePV0xMjH0HVs+ePTVixAhNnDhRO3fu1HvvvaeMjAzdddddiomJkSSNHTtWTqdTaWlp2r9/v9asWaMlS5YoMzPT7sdDDz2kvLw8LVy4UKWlpcrOztbu3buVkZHx898VAAAQ9Bo88Xj37t0aNmyY/bg+eEyYMEG5ubmaMWOGTpw4oUmTJuno0aO65ZZblJeXp7CwMPs5K1euVEZGhoYPH66QkBCNHj1af/3rX+32iIgIbdy4Uenp6Ro4cKA6dOig2bNn+6ylc9NNN2nVqlV67LHH9Oijj+q6667TunXr1Lt370t6IwAAgFl+1jo5wY51chDMmMAavFgvB/h5ArJODgAAQFNByAEAAEYi5AAAACMRcgAAgJEa9WsdAPgfE44B4OIwkgMAAIxEyAGAy4zvsAIuD0IOAAAwEiEHAAAYiZADAACMRMgBAABGIuQAAAAjEXIAAICRWAwQCBLccgwADcNIDgAAMBIhBwAChEUBAf8i5AAAACMRcgAAgJEIOQAAwEiEHAAAYCRCDgAAMBIhBwAAGImQAwAAjMSKxwAQYGeulVM+LyWAPQHMwkgOAAAwEiEHAAAYictVQBPHsv8AcGkYyQEAAEYi5AAAACMRcgAAgJEIOQAAwEiEHAAAYCRCDgA0IV1nbeCOOqCREHIAAICRGj3kdO3aVQ6H46wtPT1dkjR06NCz2iZPnuxzjIqKCqWkpKhly5aKjIzU9OnTdfr0aZ+aLVu2aMCAAXK5XLr22muVm5vb2KcCAACCWKMvBrhr1y7V1tbaj/ft26df/epX+u1vf2vvmzhxop544gn7ccuWLe2fa2trlZKSoujoaG3btk2HDx/W+PHjdeWVV+rJJ5+UJB08eFApKSmaPHmyVq5cqYKCAj3wwAPq1KmT3G53Y58SAAAIQo0ecjp27OjzeN68eerWrZt++ctf2vtatmyp6Ojocz5/48aN+uijj7Rp0yZFRUWpX79+mjt3rmbOnKns7Gw5nU6tWLFCcXFxWrhwoSSpZ8+eevfdd7Vo0SJCDgAAkOTnOTk1NTV6+eWXdf/998vhcNj7V65cqQ4dOqh3797KysrSDz/8YLcVFRUpPj5eUVFR9j632y2v16v9+/fbNUlJST6v5Xa7VVRUdMH+VFdXy+v1+mxAU1Q/+ZQJqABw6fz63VXr1q3T0aNHde+999r7xo4dqy5duigmJkZ79+7VzJkzVVZWptdee02S5PF4fAKOJPuxx+O5YI3X69XJkyfVokWLc/YnJydHc+bMaazTAwAATZhfQ87zzz+vkSNHKiYmxt43adIk++f4+Hh16tRJw4cP16effqpu3br5szvKyspSZmam/djr9So2NtavrwkAAALDbyHn888/16ZNm+wRmvNJSEiQJB04cEDdunVTdHS0du7c6VNTWVkpSfY8nujoaHvfmTXh4eHnHcWRJJfLJZfL1eBzAQAAwcdvc3JefPFFRUZGKiUl5YJ1JSUlkqROnTpJkhITE/Xhhx/qyJEjdk1+fr7Cw8PVq1cvu6agoMDnOPn5+UpMTGzEMwAAAMHMLyM5dXV1evHFFzVhwgRdccX/vcSnn36qVatWadSoUWrfvr327t2radOmaciQIerTp48kKTk5Wb169dI999yj+fPny+Px6LHHHlN6ero9CjN58mQtXbpUM2bM0P3336/NmzfrlVde0YYNTNJEcGOiMQA0Hr+M5GzatEkVFRW6//77ffY7nU5t2rRJycnJ6tGjhx5++GGNHj1ab775pl0TGhqq9evXKzQ0VImJibr77rs1fvx4n3V14uLitGHDBuXn56tv375auHChnnvuOW4fBwAANodlWVagOxEoXq9XERERqqqqUnh4eKC7AzCSA1v5vAtf6geas4v9/Oa7qwAAgJEIOQDQBLEYJPDzEXIAAICRCDkAAMBIhBwAAGAkQg4AADASIQcAmjAmIAOXzq9f0Ang4vAhBgCNj5EcAABgJEIOAAAwEiEHAAAYiZADAACMRMgBAABGIuQAAAAjEXIAAICRWCcHCCDWxwEA/yHkAEAQODMQl89LCWBPgODB5SoAAGAkQg4AADASIQcAABiJkAMAAIxEyAEAAEYi5AAAACNxCzlwmbE2DgBcHozkAAAAIxFyACDIdJ21gRFB4CIQcgAAgJEIOQAAwEiEHAAAYCRCDgAAMBIhBwAAGIl1coDLhLth0Njq/0yVz0sJcE+ApomRHAAAYCRCDgAAMBIhBwAAGKnRQ052drYcDofP1qNHD7v9xx9/VHp6utq3b6+rrrpKo0ePVmVlpc8xKioqlJKSopYtWyoyMlLTp0/X6dOnfWq2bNmiAQMGyOVy6dprr1Vubm5jnwoAAAhifhnJuf7663X48GF7e/fdd+22adOm6c0339TatWu1detWffXVV7rjjjvs9traWqWkpKimpkbbtm3TSy+9pNzcXM2ePduuOXjwoFJSUjRs2DCVlJRo6tSpeuCBB/T222/743QAAEAQ8svdVVdccYWio6PP2l9VVaXnn39eq1at0r/8y79Ikl588UX17NlT27dv14033qiNGzfqo48+0qZNmxQVFaV+/fpp7ty5mjlzprKzs+V0OrVixQrFxcVp4cKFkqSePXvq3Xff1aJFi+R2u/1xSgAAIMj4ZSTnk08+UUxMjK655hqNGzdOFRUVkqTi4mKdOnVKSUlJdm2PHj3UuXNnFRUVSZKKiooUHx+vqKgou8btdsvr9Wr//v12zZnHqK+pP8b5VFdXy+v1+mwAAMBMjR5yEhISlJubq7y8PC1fvlwHDx7UrbfeqmPHjsnj8cjpdKpNmzY+z4mKipLH45EkeTwen4BT317fdqEar9erkydPnrdvOTk5ioiIsLfY2Nife7oAAKCJavTLVSNHjrR/7tOnjxISEtSlSxe98soratGiRWO/XINkZWUpMzPTfuz1egk6AIIeiwIC5+b3FY/btGmjX/ziFzpw4IB+9atfqaamRkePHvUZzamsrLTn8ERHR2vnzp0+x6i/++rMmn++I6uyslLh4eEXDFIul0sul6sxTgu4aKx0DACB4fd1co4fP65PP/1UnTp10sCBA3XllVeqoKDAbi8rK1NFRYUSExMlSYmJifrwww915MgRuyY/P1/h4eHq1auXXXPmMepr6o8BAADQ6CHnkUce0datW1VeXq5t27bp9ttvV2hoqMaMGaOIiAilpaUpMzNT77zzjoqLi3XfffcpMTFRN954oyQpOTlZvXr10j333KMPPvhAb7/9th577DGlp6fbozCTJ0/WZ599phkzZqi0tFTPPPOMXnnlFU2bNq2xTwcAAASpRr9c9cUXX2jMmDH69ttv1bFjR91yyy3avn27OnbsKElatGiRQkJCNHr0aFVXV8vtduuZZ56xnx8aGqr169frwQcfVGJiolq1aqUJEyboiSeesGvi4uK0YcMGTZs2TUuWLNHVV1+t5557jtvHAQCAzWFZlhXoTgSK1+tVRESEqqqqFB4eHujuwFDMyUEgMAkZJrvY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fPZHRUWptLT0nM/JycnRnDlzztofGxvrlz4CAIJXxOJA9wA/5dixY4qIiDhve9CGnEuRlZWlzMxM+3FdXZ2+++47tW/fXg6HI4A9uzher1exsbE6dOgQl9cuE97zwOB9v/x4zwOD9/3SWJalY8eOKSYm5oJ1QRtyOnTooNDQUFVWVvrsr6ysVHR09Dmf43K55HK5fPa1adPGX130m/DwcP4yXGa854HB+3758Z4HBu97w11oBKde0H53ldPp1MCBA1VQUGDvq6urU0FBgRITEwPYMwAA0BQE7UiOJGVmZmrChAkaNGiQBg8erMWLF+vEiRO67777At01AAAQYEEdcu688059/fXXmj17tjwej/r166e8vLyzJiObwuVy6fHHHz/rkhv8h/c8MHjfLz/e88DgffevoF4nBwAA4HyCdk4OAADAhRByAACAkQg5AADASIQcAABgJEJOkKuurla/fv3kcDhUUlIS6O4Yrby8XGlpaYqLi1OLFi3UrVs3Pf7446qpqQl014yybNkyde3aVWFhYUpISNDOnTsD3SWj5eTk6IYbblDr1q0VGRmp1NRUlZWVBbpbzcq8efPkcDg0derUQHfFOIScIDdjxoyfXNYajaO0tFR1dXX629/+pv3792vRokVasWKFHn300UB3zRhr1qxRZmamHn/8ce3Zs0d9+/aV2+3WkSNHAt01Y23dulXp6enavn278vPzderUKSUnJ+vEiROB7lqzsGvXLv3tb39Tnz59At0VI3ELeRD7n//5H2VmZuq///u/df311+v9999Xv379At2tZmXBggVavny5Pvvss0B3xQgJCQm64YYbtHTpUkn/u4p5bGyspkyZolmzZgW4d83D119/rcjISG3dulVDhgwJdHeMdvz4cQ0YMEDPPPOM/vznP6tfv35avHhxoLtlFEZyglRlZaUmTpyo//zP/1TLli0D3Z1mq6qqSu3atQt0N4xQU1Oj4uJiJSUl2ftCQkKUlJSkoqKiAPaseamqqpIk/lxfBunp6UpJSfH5M4/GFdQrHjdXlmXp3nvv1eTJkzVo0CCVl5cHukvN0oEDB/T000/rL3/5S6C7YoRvvvlGtbW1Z61YHhUVpdLS0gD1qnmpq6vT1KlTdfPNN6t3796B7o7RVq9erT179mjXrl2B7orRGMlpQmbNmiWHw3HBrbS0VE8//bSOHTumrKysQHfZCBf7vp/pyy+/1IgRI/Tb3/5WEydODFDPgcaVnp6uffv2afXq1YHuitEOHTqkhx56SCtXrlRYWFigu2M05uQ0IV9//bW+/fbbC9Zcc801+t3vfqc333xTDofD3l9bW6vQ0FCNGzdOL730kr+7apSLfd+dTqck6auvvtLQoUN14403Kjc3VyEh/FuhMdTU1Khly5Z69dVXlZqaau+fMGGCjh49qjfeeCNwnWsGMjIy9MYbb6iwsFBxcXGB7o7R1q1bp9tvv12hoaH2vtraWjkcDoWEhKi6utqnDZeOkBOEKioq5PV67cdfffWV3G63Xn31VSUkJOjqq68OYO/M9uWXX2rYsGEaOHCgXn75ZX4RNbKEhAQNHjxYTz/9tKT/vXzSuXNnZWRkMPHYTyzL0pQpU/T6669ry5Ytuu666wLdJeMdO3ZMn3/+uc++++67Tz169NDMmTO5VNiImJMThDp37uzz+KqrrpIkdevWjYDjR19++aWGDh2qLl266C9/+Yu+/vpruy06OjqAPTNHZmamJkyYoEGDBmnw4MFavHixTpw4ofvuuy/QXTNWenq6Vq1apTfeeEOtW7eWx+ORJEVERKhFixYB7p2ZWrdufVaQadWqldq3b0/AaWSEHOAi5efn68CBAzpw4MBZYZIB0cZx55136uuvv9bs2bPl8XjUr18/5eXlnTUZGY1n+fLlkqShQ4f67H/xxRd17733Xv4OAY2Iy1UAAMBIzJgEAABGIuQAAAAjEXIAAICRCDkAAMBIhBwAAGAkQg4AADASIQcAABiJkAMAAIxEyAEAAEYi5AAAACMRcgAAgJEIOQAAwEj/DzEFCktHXYazAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "c = np.random.randn(1000000)\n",
    "\n",
    "plt.hist(c, bins=200)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.,  2.,  4.,  6.,  8.],\n",
       "       [ 1.,  3.,  5.,  7.,  9.],\n",
       "       [ 2.,  4.,  6.,  8., 10.]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Inicialización del Array utilizando una función personalizada\n",
    "\n",
    "def func(x, y):\n",
    "    return x + 2 * y\n",
    "\n",
    "np.fromfunction(func, (3, 5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Acceso a los elementos de un array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Array unidimensional"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (6,)\n",
      "Array_uni: [ 1  3  5  7  9 11]\n"
     ]
    }
   ],
   "source": [
    "# Creación de un Array unidimensional\n",
    "array_uni = np.array([1, 3, 5, 7, 9, 11])\n",
    "print(\"Shape:\", array_uni.shape)\n",
    "print(\"Array_uni:\", array_uni)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accediendo al quinto elemento del Array\n",
    "array_uni[4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 7])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accediendo al tercer y cuarto elemento del Array\n",
    "array_uni[2:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 7])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accediendo a los elementos 0, 3 y 5 del Array\n",
    "array_uni[0::3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Array multidimensional"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (2, 4)\n",
      "Array_multi:\n",
      " [[1 2 3 4]\n",
      " [5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "# Creación de un Array multidimensional\n",
    "array_multi = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])\n",
    "print(\"Shape:\", array_multi.shape)\n",
    "print(\"Array_multi:\\n\", array_multi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accediendo al cuarto elemento del Array\n",
    "array_multi[0, 3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 6, 7, 8])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accediendo a la segunda fila del Array\n",
    "array_multi[1, :]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 7])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accediendo al tercer elemento de las dos primeras filas del Array\n",
    "array_multi[0:2, 2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Modificación de un Array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (28,)\n",
      "Array 1: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n",
      " 24 25 26 27]\n"
     ]
    }
   ],
   "source": [
    "# Creación de un Array unidimensional inicializado con el rango de elementos 0-27\n",
    "array1 = np.arange(28)\n",
    "print(\"Shape:\", array1.shape)\n",
    "print(\"Array 1:\", array1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (7, 4)\n",
      "Array 1:\n",
      " [[ 0  1  2  3]\n",
      " [ 4  5  6  7]\n",
      " [ 8  9 10 11]\n",
      " [12 13 14 15]\n",
      " [16 17 18 19]\n",
      " [20 21 22 23]\n",
      " [24 25 26 27]]\n"
     ]
    }
   ],
   "source": [
    "# Cambiar las dimensiones del Array y sus longitudes\n",
    "array1.shape = (7, 4)\n",
    "print(\"Shape:\", array1.shape)\n",
    "print(\"Array 1:\\n\", array1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (4, 7)\n",
      "Array 2:\n",
      " [[ 0  1  2  3  4  5  6]\n",
      " [ 7  8  9 10 11 12 13]\n",
      " [14 15 16 17 18 19 20]\n",
      " [21 22 23 24 25 26 27]]\n"
     ]
    }
   ],
   "source": [
    "# El ejemplo anterior devuelve un nuevo Array que apunta a los mismos datos. \n",
    "# Importante: Modificaciones en un Array, modificaran el otro Array\n",
    "array2 = array1.reshape(4, 7)\n",
    "print(\"Shape:\", array2.shape)\n",
    "print(\"Array 2:\\n\", array2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 2:\n",
      " [[ 0  1  2 20  4  5  6]\n",
      " [ 7  8  9 10 11 12 13]\n",
      " [14 15 16 17 18 19 20]\n",
      " [21 22 23 24 25 26 27]]\n"
     ]
    }
   ],
   "source": [
    "# Modificación del nuevo Array devuelto\n",
    "array2[0, 3] = 20\n",
    "print(\"Array 2:\\n\", array2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 1:\n",
      " [[ 0  1  2 20]\n",
      " [ 4  5  6  7]\n",
      " [ 8  9 10 11]\n",
      " [12 13 14 15]\n",
      " [16 17 18 19]\n",
      " [20 21 22 23]\n",
      " [24 25 26 27]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Array 1:\\n\", array1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 1: [ 0  1  2 20  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n",
      " 24 25 26 27]\n"
     ]
    }
   ],
   "source": [
    "# Desenvuelve el Array, devolviendo un nuevo Array de una sola dimension\n",
    "# Importante: El nuevo array apunta a los mismos datos\n",
    "print(\"Array 1:\", array1.ravel())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Operaciones aritméticas con Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 1: [ 2  4  6  8 10 12 14 16]\n",
      "Array 2: [0 1 2 3 4 5 6 7]\n"
     ]
    }
   ],
   "source": [
    "# Creación de dos Arrays unidimensionales\n",
    "array1 = np.arange(2, 18, 2)\n",
    "array2 = np.arange(8)\n",
    "print(\"Array 1:\", array1)\n",
    "print(\"Array 2:\", array2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  5  8 11 14 17 20 23]\n"
     ]
    }
   ],
   "source": [
    "# Suma\n",
    "print(array1 + array2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "# Resta\n",
    "print(array1 - array2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[  0   4  12  24  40  60  84 112]\n"
     ]
    }
   ],
   "source": [
    "# Multiplicacion\n",
    "# Importante: No es una multiplicación de matrices\n",
    "print(array1 * array2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Broadcasting"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Si se aplican operaciones aritméticas sobre Arrays que no tienen la misma forma (shape) Numpy aplica un propiedad que se denomina Broadcasting."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape Array 1: (5,)\n",
      "Array 1: [0 1 2 3 4]\n",
      "\n",
      "Shape Array 2: (1,)\n",
      "Array 2: [3]\n"
     ]
    }
   ],
   "source": [
    "# Creación de dos Arrays unidimensionales\n",
    "array1 = np.arange(5)\n",
    "array2 = np.array([3])\n",
    "print(\"Shape Array 1:\", array1.shape)\n",
    "print(\"Array 1:\", array1)\n",
    "print()\n",
    "print(\"Shape Array 2:\", array2.shape)\n",
    "print(\"Array 2:\", array2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 4, 5, 6, 7])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Suma de ambos Arrays\n",
    "array1 + array2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape Array 1: (2, 3)\n",
      "Array 1:\n",
      " [[0 1 2]\n",
      " [3 4 5]]\n",
      "\n",
      "Shape Array 2: (3,)\n",
      "Array 2: [ 6 10 14]\n"
     ]
    }
   ],
   "source": [
    "# Creación de dos Arrays multidimensional y unidimensional\n",
    "array1 = np.arange(6)\n",
    "array1.shape = (2, 3)\n",
    "array2 = np.arange(6, 18, 4)\n",
    "print(\"Shape Array 1:\", array1.shape)\n",
    "print(\"Array 1:\\n\", array1)\n",
    "print()\n",
    "print(\"Shape Array 2:\", array2.shape)\n",
    "print(\"Array 2:\", array2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 6, 11, 16],\n",
       "       [ 9, 14, 19]])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Suma de ambos Arrays\n",
    "array1 + array2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Funciones estadísticas sobre Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 1: [ 1  3  5  7  9 11 13 15 17 19]\n"
     ]
    }
   ],
   "source": [
    "# Creación de un Array unidimensional\n",
    "array1 = np.arange(1, 20, 2)\n",
    "print(\"Array 1:\", array1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10.0"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Media de los elementos del Array\n",
    "array1.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Suma de los elementos del Array\n",
    "array1.sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Funciones universales eficientes proporcionadas por numpy: **ufunc**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1,   9,  25,  49,  81, 121, 169, 225, 289, 361])"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Cuadrado de los elementos del Array\n",
    "np.square(array1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.        , 1.73205081, 2.23606798, 2.64575131, 3.        ,\n",
       "       3.31662479, 3.60555128, 3.87298335, 4.12310563, 4.35889894])"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Raiz cuadrada de los elementos del Array\n",
    "np.sqrt(array1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2.71828183e+00, 2.00855369e+01, 1.48413159e+02, 1.09663316e+03,\n",
       "       8.10308393e+03, 5.98741417e+04, 4.42413392e+05, 3.26901737e+06,\n",
       "       2.41549528e+07, 1.78482301e+08])"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exponencial de los elementos del Array\n",
    "np.exp(array1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.        , 1.09861229, 1.60943791, 1.94591015, 2.19722458,\n",
       "       2.39789527, 2.56494936, 2.7080502 , 2.83321334, 2.94443898])"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# log de los elementos del Array\n",
    "np.log(array1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}