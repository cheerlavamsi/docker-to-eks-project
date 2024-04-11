variable "region" {
  description = "The AWS region where the resources will be provisioned."
  type        = string
  default     = "us-west-2"
}

variable "instance_type" {
  description = "The EC2 instance type."
  type        = string
  default     = "t2.micro"
}

variable "ami" {
  description = "The AMI ID for the EC2 instance."
  type        = string
  default     = "ami-12345678"
}

variable "subnet_id" {
  description = "The ID of the subnet where the EC2 instance will be launched."
  type        = string
}
