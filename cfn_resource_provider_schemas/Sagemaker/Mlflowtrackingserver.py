SCHEMA = {
  "typeName" : "AWS::SageMaker::MlflowTrackingServer",
  "description" : "Resource Type definition for AWS::SageMaker::MlflowTrackingServer",
  "additionalProperties" : False,
  "properties" : {
    "TrackingServerName" : {
      "type" : "string",
      "description" : "The name of the MLFlow Tracking Server.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}$"
    },
    "TrackingServerArn" : {
      "description" : "The Amazon Resource Name (ARN) of the MLFlow Tracking Server.",
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "^arn:aws[a-z\\-]*:sagemaker:[a-z0-9\\-]*:[0-9]{12}:mlflow-tracking-server/.*$"
    },
    "TrackingServerSize" : {
      "type" : "string",
      "description" : "The size of the MLFlow Tracking Server.",
      "enum" : [ "Small", "Medium", "Large" ]
    },
    "MlflowVersion" : {
      "type" : "string",
      "description" : "The MLFlow Version used on the MLFlow Tracking Server.",
      "minLength" : 1,
      "maxLength" : 32,
      "pattern" : "^\\d+(\\.\\d+)+$"
    },
    "RoleArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on behalf of the customer.",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "^arn:aws[a-z\\-]*:iam::\\d{12}:role\\/?[a-zA-Z_0-9+=,.@\\-_\\/]+$"
    },
    "ArtifactStoreUri" : {
      "type" : "string",
      "description" : "The Amazon S3 URI for MLFlow Tracking Server artifacts.",
      "minLength" : 1,
      "maxLength" : 2048,
      "pattern" : "^s3:\\/\\/([^\\/]+)\\/?(.*)$"
    },
    "AutomaticModelRegistration" : {
      "type" : "boolean",
      "description" : "A flag to enable Automatic SageMaker Model Registration."
    },
    "WeeklyMaintenanceWindowStart" : {
      "type" : "string",
      "description" : "The start of the time window for maintenance of the MLFlow Tracking Server in UTC time.",
      "pattern" : "^(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\\d|2[0-3]):([0-5]\\d)$",
      "maxLength" : 9
    },
    "Tags" : {
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 50,
      "description" : "An array of key-value pairs to apply to this resource.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A key-value pair to associate with a resource.",
      "properties" : {
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "maxLength" : 256
        },
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "TrackingServerName", "ArtifactStoreUri", "RoleArn" ],
  "conditionalCreateOnlyProperties" : [ "/properties/MlflowVersion", "/properties/RoleArn" ],
  "createOnlyProperties" : [ "/properties/TrackingServerName" ],
  "primaryIdentifier" : [ "/properties/TrackingServerName" ],
  "readOnlyProperties" : [ "/properties/TrackingServerArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "sagemaker:AddTags", "sagemaker:ListTags", "sagemaker:DeleteTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:CreateMlflowTrackingServer", "sagemaker:DescribeMlflowTrackingServer", "sagemaker:AddTags", "sagemaker:ListTags", "iam:PassRole" ],
      "timeoutInMinutes" : 95
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeMlflowTrackingServer", "sagemaker:ListTags" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateMlflowTrackingServer", "sagemaker:DescribeMlflowTrackingServer", "sagemaker:ListTags", "sagemaker:AddTags", "sagemaker:DeleteTags", "iam:PassRole" ],
      "timeoutInMinutes" : 65
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeleteMlflowTrackingServer", "sagemaker:DescribeMlflowTrackingServer" ],
      "timeoutInMinutes" : 95
    },
    "list" : {
      "permissions" : [ "sagemaker:ListMlflowTrackingServers" ]
    }
  }
}