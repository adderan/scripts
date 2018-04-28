library(dplyr)
library(ggplot2)

insertions.vs.branch.length <- function(insertion.lengths.file, branch.lengths.file, out.file) {
  insertion.lengths <- read.table(insertion.lengths.file)
  colnames(insertion.lengths) <- c("branch", "length")

  nInsertions <- insertion.lengths %>% count(branch)
  nInsertions <- subset(nInsertions, branch != "root")

  branch.lengths <- data.frame(read.table(branch.lengths.file))
  colnames(branch.lengths) <- c("branch", "branch.length")
  data <- merge(nInsertions, branch.lengths, by=c("branch"))
  plot <- ggplot(data, aes(x=branch.length, y=n)) + geom_point() + ylim(0,1500000) + xlim(0, 0.4)

  png(out.file, width=800, height=800)
  print(plot)
  dev.off()
}
