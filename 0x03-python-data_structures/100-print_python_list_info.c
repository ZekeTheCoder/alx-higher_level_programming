#include <stdio.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about
 * Python lists.
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %li\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %i: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
