library(ggplot2)

selected.insertions.plot <- function(all.file, selected.file, out.file) {
  all.lengths <- read.table(all.file)
  selected.lengths <- read.table(selected.file)
  selected.lengths <- data.frame(length = selected.lengths[,5] - selected.lengths[,4])
  selected.lengths$label <- "Selected"

  colnames(all.lengths) <- c("label", "length")
  all.lengths$label <- "All"


  lengths <- rbind(all.lengths, selected.lengths)


  png(out.file, width=800, height=600)

  plot <- ggplot(lengths, aes(x=length, fill=label)) + geom_density(alpha=0.4) + xlim(0,1000)
  print(plot)

  dev.off()
}


