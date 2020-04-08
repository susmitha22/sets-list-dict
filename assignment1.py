{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 1, 20.5, 'susmitha', [1, 3, 4, 6]]\n"
     ]
    }
   ],
   "source": [
    "list1=[1,1,20.5,\"susmitha\",[1,3,4,6]]\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 1, 20.5, 'susmitha', [1, 3, 4, 6], 10, [10]]\n"
     ]
    }
   ],
   "source": [
    "list1.append([10])\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(list1.count(1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2', 1, 20.5, 'susmitha', [1, 3, 4, 6], 10, [10]]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "copy1=list1[:]\n",
    "copy1[0]='2'\n",
    "print(copy1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 1, 20.5, 'susmitha', [1, 3, 4, 6], 10, [10], 17, 56]\n"
     ]
    }
   ],
   "source": [
    "list1.extend([17,56])\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "print(list1.index(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[52, 56, 34, 34, 1, 34, 34, 'hindhuja', 'hindhuja', 1, 20.5, 'susmitha', [1, 3, 4, 6], 10, [10], 17, 56, 67]\n"
     ]
    }
   ],
   "source": [
    "list1.insert(0,52)\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[52, 56, 34, 34, 1, 34, 34, 'hindhuja', 'hindhuja', 1, 20.5, 'susmitha']\n"
     ]
    }
   ],
   "source": [
    "list1.pop()\n",
    "list1.pop()\n",
    "list1.pop()\n",
    "list1.pop()\n",
    "list1.pop()\n",
    "\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[52, 34, 34, 1, 34, 34, 'hindhuja', 'hindhuja', 1, 20.5, 'susmitha']\n"
     ]
    }
   ],
   "source": [
    "list1.remove(56)\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['susmitha', 20.5, 1, 'hindhuja', 'hindhuja', 34, 34, 1, 34, 34, 52]\n"
     ]
    }
   ],
   "source": [
    "list1.reverse()\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "list1.clear()\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'susmitha', 'age': 19, 2: 19, 7: 56}\n"
     ]
    }
   ],
   "source": [
    "dict={'name':'susmitha','age':19,2:19,7:56}\n",
    "print(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n",
      "{'name': 'susmitha', 'age': 19, 7: 56}\n",
      "(7, 56)\n",
      "{'name': 'susmitha', 'age': 19}\n"
     ]
    }
   ],
   "source": [
    "print(dict.pop(2))\n",
    "print(dict)\n",
    "print(dict.popitem())\n",
    "print(dict)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "dict.clear()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'hi': 0, 'susmitha': 0}\n"
     ]
    }
   ],
   "source": [
    "marks={}.fromkeys(['hi','susmitha'],0)\n",
    "print(marks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 35, 2: 90, 7: 78}\n"
     ]
    }
   ],
   "source": [
    "dict={1:35,2:56,7:78}\n",
    "d1={2:90}\n",
    "dict.update(d1)\n",
    "print(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35\n"
     ]
    }
   ],
   "source": [
    "print(dict.get(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 35, 2: 90, 7: 78}\n"
     ]
    }
   ],
   "source": [
    "dict1=dict.copy()\n",
    "print(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{2, 3, 4}\n"
     ]
    }
   ],
   "source": [
    "set={2,3,4}\n",
    "print(set)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{2, 3, 4, 15}\n"
     ]
    }
   ],
   "source": [
    "set.add(15)\n",
    "print (set)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{3, 4, 15}\n"
     ]
    }
   ],
   "source": [
    "set.difference_update([2,5,7])\n",
    "print(set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{4}\n"
     ]
    }
   ],
   "source": [
    "set.intersection_update([2,4,10])\n",
    "print(set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{3, 4}\n",
      "{3, 4}\n"
     ]
    }
   ],
   "source": [
    "a={2,3,4}\n",
    "b={3,4,6}\n",
    "print(a.intersection(b))\n",
    "print(b.intersection(a))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{2}\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(a.difference(b))\n",
    "print(a.difference_update(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(a.issubset(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(a.isdisjoint(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
