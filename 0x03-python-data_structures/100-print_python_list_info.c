#include <Python.h>
#include <object.h>
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
	int i;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		item = obj->ob_item[i];
		printf("Element %i: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
