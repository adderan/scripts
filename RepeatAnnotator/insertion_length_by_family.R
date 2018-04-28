library(ggplot2)

insertion.length.by.family <- function(gff.file, out.file) {
  lengths <- read.table(gff.file)
  lengths <- data.frame(length = lengths[,5] - lengths[,4], label = lengths[,9])


  family.sizes <- data.frame(table(lengths$label))
  colnames(family.sizes) <- c("Family", "Size")


  new.lengths <- data.frame()
  #delete features in small families
  for (i in 1:nrow(lengths)) {
    family <- lengths[i,2]
    family.size <- family.sizes[family.sizes$Family == family, ]$Size
    print(family.size)
    print(lengths[i,])
    if (family.size > 10) {
      new.lengths <- rbind(new.lengths, lengths[i,])
    }
  }
  print(new.lengths)
    

  png(out.file, width=800, height=600)
  plot <- ggplot(new.lengths, aes(x=new.lengths$length, fill=new.lengths$label)) + geom_density(alpha=0.4) + xlim(0,500)
  print(plot)

  dev.off()
}

