SCHEMA = {
  "typeName" : "AWS::SageMaker::DeviceFleet",
  "description" : "Resource schema for AWS::SageMaker::DeviceFleet",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sagemaker-edge.git",
  "definitions" : {
    "EdgeOutputConfig" : {
      "type" : "object",
      "properties" : {
        "S3OutputLocation" : {
          "description" : "The Amazon Simple Storage (S3) bucket URI",
          "type" : "string",
          "pattern" : "^s3://([^/]+)/?(.*)$",
          "maxLength" : 1024
        },
        "KmsKeyId" : {
          "description" : "The KMS key id used for encryption on the S3 bucket",
          "type" : "string",
          "pattern" : "[a-zA-Z0-9:_-]+",
          "minLength" : 1,
          "maxLength" : 2048
        }
      },
      "required" : [ "S3OutputLocation" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "Key-value pair to associate as a tag for the resource",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "type" : "string",
          "pattern" : "^((?!aws:)[\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "The key value of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "type" : "string",
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Description" : {
      "description" : "Description for the edge device fleet",
      "type" : "string",
      "pattern" : "[\\S\\s]+",
      "minLength" : 0,
      "maxLength" : 800
    },
    "DeviceFleetName" : {
      "description" : "The name of the edge device fleet",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "OutputConfig" : {
      "description" : "S3 bucket and an ecryption key id (if available) to store outputs for the fleet",
      "$ref" : "#/definitions/EdgeOutputConfig"
    },
    "RoleArn" : {
      "description" : "Role associated with the device fleet",
      "type" : "string",
      "pattern" : "^arn:aws[a-z\\-]*:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+$",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "Tags" : {
      "description" : "Associate tags with the resource",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "DeviceFleetName", "OutputConfig", "RoleArn" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/DeviceFleetName" ],
  "createOnlyProperties" : [ "/properties/DeviceFleetName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:CreateDeviceFleet", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeDeviceFleet" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateDeviceFleet", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeleteDeviceFleet" ]
    }
  }
}