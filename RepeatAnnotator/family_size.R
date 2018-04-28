library(ggplot2)

family.size.plot <- function(gff.file, out.file) {
  gff <- read.table(gff.file)
  colnames(gff) <- c("chrom", "source", "type", "start", "end", "score", "strand", "a", "family")
  family.size <- data.frame(table(gff$family))
  colnames(family.size) <- c("Cluster", "Size")

  plot <- ggplot(family.size, aes(x=Cluster, y=Size)) + geom_bar(stat="identity")

  png(out.file, width=900, height=900)
  print(plot)
  dev.off()
}

