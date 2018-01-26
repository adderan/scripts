#include <stdio.h>
#include "sonLib.h"

typedef struct {
  char *chr;
  int start;
  int end;
  int group;
} Feature;


stList *readGff(FILE *file) {
  stList *features = stList_construct();

  char *line = NULL;
  size_t len = 0;
  while((getline(&line, &len, file) != NULL)) {
    char chr[10];
    char source[100];
    char type[100];
    int start;
    int end;
    int score;
    char strand;
    char a;
    int group;

    sscanf("%s %s %s %d %d %d %c %c %d", line, chr, source,
        type, &start, &end, &score, &strand, &a, &group);
    Feature *f = (Feature*)malloc(sizeof(Feature));
    f->chr = chr;
    f->start = start;
    f->end = end;
    f->group = group;
    stList_append(f);

  }
  return features;
}

bool featureOverlap(Feature *f1, Feature *f2) {
  bool left = (f1->start <= f2->start) && (f1->end >= f2->start);
  bool center = (f1->start >= f2->start) && (f1->end <= f2->end);
  bool right = (f1->start <= f2->end) && (f1->end >= f2->end);
  return (left || center || right);
}

int main(int argc, char **argv) {
  FILE *gff1 = fopen(argv[1]);
  FILE *gff2 = fopen(argv[2]);
  stList *X = readGff(gff1);
  stList *Y = readGff(gff2);

  for (int i = 0; i < stList_length(X); i++) {
    for (int j = 0; j < stList_length(Y); j++) {

      Feature *f1 = stList_get(X, i);
      Feature *f2 = stList_get(Y, j);
      if (featureOverlap(f1, f2)) {
      }

}
