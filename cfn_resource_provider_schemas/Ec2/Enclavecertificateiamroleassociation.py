SCHEMA = {
  "typeName" : "AWS::EC2::EnclaveCertificateIamRoleAssociation",
  "description" : "Associates an AWS Identity and Access Management (IAM) role with an AWS Certificate Manager (ACM) certificate. This association is based on Amazon Resource Names and it enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2-acmcerts.git",
  "properties" : {
    "CertificateArn" : {
      "description" : "The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.",
      "type" : "string",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:acm:[A-Za-z0-9-]{1,64}:([0-9]{12})?:certificate/.+$",
      "minLength" : 1,
      "maxLength" : 1283
    },
    "RoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.",
      "type" : "string",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:iam:.*:([0-9]{12})?:role/.+$",
      "minLength" : 1,
      "maxLength" : 1283
    },
    "CertificateS3BucketName" : {
      "description" : "The name of the Amazon S3 bucket to which the certificate was uploaded.",
      "type" : "string"
    },
    "CertificateS3ObjectKey" : {
      "description" : "The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored.",
      "type" : "string"
    },
    "EncryptionKmsKeyId" : {
      "description" : "The ID of the AWS KMS CMK used to encrypt the private key of the certificate.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "CertificateArn", "RoleArn" ],
  "primaryIdentifier" : [ "/properties/CertificateArn", "/properties/RoleArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AssociateEnclaveCertificateIamRole", "ec2:GetAssociatedEnclaveCertificateIamRoles" ]
    },
    "read" : {
      "permissions" : [ "ec2:GetAssociatedEnclaveCertificateIamRoles" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DisassociateEnclaveCertificateIamRole", "ec2:GetAssociatedEnclaveCertificateIamRoles" ]
    },
    "list" : {
      "permissions" : [ "ec2:GetAssociatedEnclaveCertificateIamRoles" ]
    }
  },
  "readOnlyProperties" : [ "/properties/CertificateS3BucketName", "/properties/CertificateS3ObjectKey", "/properties/EncryptionKmsKeyId" ],
  "createOnlyProperties" : [ "/properties/CertificateArn", "/properties/RoleArn" ]
}