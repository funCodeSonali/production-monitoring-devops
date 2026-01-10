output "ec2_public_ip" {
  value = aws_instance.monitoring_ec2.public_ip
}