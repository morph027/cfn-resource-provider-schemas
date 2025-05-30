SCHEMA = {
  "typeName" : "AWS::Personalize::DatasetGroup",
  "description" : "Resource Schema for AWS::Personalize::DatasetGroup.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-personalize",
  "properties" : {
    "DatasetGroupArn" : {
      "description" : "The Amazon Resource Name (ARN) of the dataset group.",
      "type" : "string",
      "pattern" : "arn:([a-z\\d-]+):personalize:.*:.*:.+",
      "maxLength" : 256
    },
    "Name" : {
      "description" : "The name for the new dataset group.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*"
    },
    "KmsKeyArn" : {
      "description" : "The Amazon Resource Name(ARN) of a AWS Key Management Service (KMS) key used to encrypt the datasets.",
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "arn:aws.*:kms:.*:[0-9]{12}:key/.*"
    },
    "RoleArn" : {
      "description" : "The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.",
      "type" : "string",
      "pattern" : "arn:([a-z\\d-]+):iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+",
      "minLength" : 0,
      "maxLength" : 256
    },
    "Domain" : {
      "description" : "The domain of a Domain dataset group.",
      "type" : "string",
      "enum" : [ "ECOMMERCE", "VIDEO_ON_DEMAND" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/RoleArn", "/properties/KmsKeyArn", "/properties/Domain" ],
  "readOnlyProperties" : [ "/properties/DatasetGroupArn" ],
  "primaryIdentifier" : [ "/properties/DatasetGroupArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "personalize:CreateDatasetGroup", "personalize:DescribeDatasetGroup", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "personalize:DescribeDatasetGroup" ]
    },
    "delete" : {
      "permissions" : [ "personalize:DescribeDatasetGroup", "personalize:DeleteDatasetGroup" ]
    },
    "list" : {
      "permissions" : [ "personalize:ListDatasetGroups" ]
    }
  }
}