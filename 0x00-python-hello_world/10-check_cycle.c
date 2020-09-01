#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a S.L.L have a cycle
 * @list: pointer to head
 * Return: 0 if there is no cycle 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *front, *ffront;

	if (list == NULL)
		return (0);
	front = list;
	ffront = list;
	while (ffront->next != NULL && ffront->next->next != NULL)
	{
		front = front->next;
		ffront = ffront->next->next;
		if (front == ffront)
			return (1);
	}
	return (0);
}
