SCHEMA = {
  "typeName" : "AWS::Personalize::Dataset",
  "description" : "Resource schema for AWS::Personalize::Dataset.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-personalize",
  "definitions" : {
    "DatasetImportJob" : {
      "description" : "Initial DatasetImportJob for the created dataset",
      "type" : "object",
      "properties" : {
        "JobName" : {
          "description" : "The name for the dataset import job.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*",
          "minLength" : 1,
          "maxLength" : 63
        },
        "DatasetImportJobArn" : {
          "description" : "The ARN of the dataset import job",
          "type" : "string",
          "pattern" : "arn:([a-z\\d-]+):personalize:.*:.*:.+",
          "maxLength" : 256
        },
        "DatasetArn" : {
          "description" : "The ARN of the dataset that receives the imported data",
          "type" : "string",
          "pattern" : "arn:([a-z\\d-]+):personalize:.*:.*:.+",
          "maxLength" : 256
        },
        "DataSource" : {
          "type" : "object",
          "description" : "The Amazon S3 bucket that contains the training data to import.",
          "properties" : {
            "DataLocation" : {
              "description" : "The path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored.",
              "type" : "string",
              "maxLength" : 256,
              "pattern" : "(s3|http|https)://.+"
            }
          },
          "additionalProperties" : False
        },
        "RoleArn" : {
          "description" : "The ARN of the IAM role that has permissions to read from the Amazon S3 data source.",
          "type" : "string",
          "maxLength" : 256,
          "pattern" : "arn:([a-z\\d-]+):iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name for the dataset",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*",
      "minLength" : 1,
      "maxLength" : 63
    },
    "DatasetArn" : {
      "description" : "The ARN of the dataset",
      "type" : "string",
      "pattern" : "arn:([a-z\\d-]+):personalize:.*:.*:.+",
      "maxLength" : 256
    },
    "DatasetType" : {
      "description" : "The type of dataset",
      "type" : "string",
      "enum" : [ "Interactions", "Items", "Users" ],
      "maxLength" : 256
    },
    "DatasetGroupArn" : {
      "description" : "The Amazon Resource Name (ARN) of the dataset group to add the dataset to",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:([a-z\\d-]+):personalize:.*:.*:.+"
    },
    "SchemaArn" : {
      "description" : "The ARN of the schema to associate with the dataset. The schema defines the dataset fields.",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:([a-z\\d-]+):personalize:.*:.*:.+"
    },
    "DatasetImportJob" : {
      "$ref" : "#/definitions/DatasetImportJob"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "DatasetType", "DatasetGroupArn", "SchemaArn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/DatasetType", "/properties/DatasetGroupArn", "/properties/SchemaArn" ],
  "replacementStrategy" : "delete_then_create",
  "taggable" : False,
  "readOnlyProperties" : [ "/properties/DatasetArn" ],
  "primaryIdentifier" : [ "/properties/DatasetArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "personalize:CreateDataset", "personalize:DescribeDataset", "personalize:CreateDatasetImportJob", "personalize:DescribeDatasetImportJob", "iam:PassRole" ],
      "timeoutInMinutes" : 2160
    },
    "read" : {
      "permissions" : [ "personalize:DescribeDataset" ]
    },
    "update" : {
      "permissions" : [ "personalize:DescribeDataset", "personalize:CreateDatasetImportJob", "personalize:DescribeDatasetImportJob", "iam:PassRole" ],
      "timeoutInMinutes" : 2160
    },
    "delete" : {
      "permissions" : [ "personalize:DeleteDataset", "personalize:DescribeDataset" ]
    },
    "list" : {
      "permissions" : [ "personalize:ListDatasets" ]
    }
  }
}