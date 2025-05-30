SCHEMA = {
  "typeName" : "AWS::SageMaker::InferenceExperiment",
  "description" : "Resource Type definition for AWS::SageMaker::InferenceExperiment",
  "additionalProperties" : False,
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the inference experiment.",
      "type" : "string",
      "pattern" : "^arn:aws[a-z\\-]*:sagemaker:[a-z0-9\\-]*:[0-9]{12}:inference-experiment/[a-zA-Z_0-9+=,.@\\-_/]+$",
      "minLength" : 20,
      "maxLength" : 256
    },
    "Name" : {
      "description" : "The name for the inference experiment.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 120
    },
    "Type" : {
      "description" : "The type of the inference experiment that you want to run.",
      "type" : "string",
      "enum" : [ "ShadowMode" ]
    },
    "Description" : {
      "description" : "The description of the inference experiment.",
      "type" : "string",
      "pattern" : ".*",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "RoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.",
      "type" : "string",
      "pattern" : "^arn:aws[a-z\\-]*:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+$",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "EndpointName" : {
      "$ref" : "#/definitions/EndpointName"
    },
    "EndpointMetadata" : {
      "$ref" : "#/definitions/EndpointMetadata"
    },
    "Schedule" : {
      "$ref" : "#/definitions/InferenceExperimentSchedule"
    },
    "KmsKey" : {
      "type" : "string",
      "description" : "The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.",
      "pattern" : ".*",
      "maxLength" : 2048
    },
    "DataStorageConfig" : {
      "$ref" : "#/definitions/DataStorageConfig"
    },
    "ModelVariants" : {
      "type" : "array",
      "description" : "An array of ModelVariantConfig objects. Each ModelVariantConfig object in the array describes the infrastructure configuration for the corresponding variant.",
      "maxItems" : 2,
      "items" : {
        "$ref" : "#/definitions/ModelVariantConfig"
      }
    },
    "ShadowModeConfig" : {
      "$ref" : "#/definitions/ShadowModeConfig"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "CreationTime" : {
      "description" : "The timestamp at which you created the inference experiment.",
      "type" : "string"
    },
    "LastModifiedTime" : {
      "description" : "The timestamp at which you last modified the inference experiment.",
      "type" : "string"
    },
    "Status" : {
      "description" : "The status of the inference experiment.",
      "type" : "string",
      "enum" : [ "Creating", "Created", "Updating", "Starting", "Stopping", "Running", "Completed", "Cancelled" ]
    },
    "StatusReason" : {
      "description" : "The error message or client-specified reason from the StopInferenceExperiment API, that explains the status of the inference experiment.",
      "type" : "string",
      "pattern" : ".*",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "DesiredState" : {
      "description" : "The desired state of the experiment after starting or stopping operation.",
      "type" : "string",
      "enum" : [ "Running", "Completed", "Cancelled" ]
    }
  },
  "definitions" : {
    "EndpointName" : {
      "description" : "The name of the endpoint used to run the inference experiment.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*",
      "maxLength" : 63
    },
    "EndpointMetadata" : {
      "description" : "The metadata of the endpoint on which the inference experiment ran.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EndpointName" : {
          "$ref" : "#/definitions/EndpointName"
        },
        "EndpointConfigName" : {
          "description" : "The name of the endpoint configuration.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*",
          "maxLength" : 63
        },
        "EndpointStatus" : {
          "description" : "The status of the endpoint. For possible values of the status of an endpoint.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*",
          "enum" : [ "Creating", "Updating", "SystemUpdating", "RollingBack", "InService", "OutOfService", "Deleting", "Failed" ]
        }
      },
      "required" : [ "EndpointName" ]
    },
    "CaptureContentTypeHeader" : {
      "description" : "Configuration specifying how to treat different headers. If no headers are specified SageMaker will by default base64 encode when capturing the data.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CsvContentTypes" : {
          "description" : "The list of all content type headers that SageMaker will treat as CSV and capture accordingly.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 10,
          "items" : {
            "type" : "string",
            "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*/[a-zA-Z0-9](-*[a-zA-Z0-9.])*",
            "minLength" : 1,
            "maxLength" : 256
          }
        },
        "JsonContentTypes" : {
          "description" : "The list of all content type headers that SageMaker will treat as JSON and capture accordingly.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 10,
          "items" : {
            "type" : "string",
            "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*/[a-zA-Z0-9](-*[a-zA-Z0-9.])*",
            "minLength" : 1,
            "maxLength" : 256
          }
        }
      }
    },
    "DataStorageConfig" : {
      "description" : "The Amazon S3 location and configuration for storing inference request and response data.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "description" : "The Amazon S3 bucket where the inference request and response data is stored.",
          "type" : "string",
          "pattern" : "^(https|s3)://([^/])/?(.*)$",
          "maxLength" : 512
        },
        "KmsKey" : {
          "description" : "The AWS Key Management Service key that Amazon SageMaker uses to encrypt captured data at rest using Amazon S3 server-side encryption.",
          "type" : "string",
          "pattern" : ".*",
          "maxLength" : 2048
        },
        "ContentType" : {
          "$ref" : "#/definitions/CaptureContentTypeHeader"
        }
      },
      "required" : [ "Destination" ]
    },
    "InferenceExperimentSchedule" : {
      "description" : "The duration for which you want the inference experiment to run.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StartTime" : {
          "description" : "The timestamp at which the inference experiment started or will start.",
          "type" : "string"
        },
        "EndTime" : {
          "description" : "The timestamp at which the inference experiment ended or will end.",
          "type" : "string"
        }
      }
    },
    "RealTimeInferenceConfig" : {
      "description" : "The infrastructure configuration for deploying the model to a real-time inference endpoint.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InstanceType" : {
          "description" : "The instance type the model is deployed to.",
          "type" : "string"
        },
        "InstanceCount" : {
          "description" : "The number of instances of the type specified by InstanceType.",
          "type" : "integer"
        }
      },
      "required" : [ "InstanceType", "InstanceCount" ]
    },
    "ModelInfrastructureConfig" : {
      "description" : "The configuration for the infrastructure that the model will be deployed to.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InfrastructureType" : {
          "description" : "The type of the inference experiment that you want to run.",
          "type" : "string",
          "enum" : [ "RealTimeInference" ]
        },
        "RealTimeInferenceConfig" : {
          "$ref" : "#/definitions/RealTimeInferenceConfig"
        }
      },
      "required" : [ "InfrastructureType", "RealTimeInferenceConfig" ]
    },
    "ModelVariantConfig" : {
      "description" : "Contains information about the deployment options of a model.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ModelName" : {
          "description" : "The name of the Amazon SageMaker Model entity.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*",
          "maxLength" : 63
        },
        "VariantName" : {
          "description" : "The name of the variant.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9]([\\-a-zA-Z0-9]*[a-zA-Z0-9])?",
          "maxLength" : 63
        },
        "InfrastructureConfig" : {
          "$ref" : "#/definitions/ModelInfrastructureConfig"
        }
      },
      "required" : [ "ModelName", "VariantName", "InfrastructureConfig" ]
    },
    "ShadowModelVariantConfig" : {
      "description" : "The name and sampling percentage of a shadow variant.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ShadowModelVariantName" : {
          "description" : "The name of the shadow variant.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9]([\\-a-zA-Z0-9]*[a-zA-Z0-9])?",
          "maxLength" : 63
        },
        "SamplingPercentage" : {
          "description" : "The percentage of inference requests that Amazon SageMaker replicates from the production variant to the shadow variant.",
          "type" : "integer",
          "maximum" : 100
        }
      },
      "required" : [ "ShadowModelVariantName", "SamplingPercentage" ]
    },
    "ShadowModeConfig" : {
      "description" : "The configuration of ShadowMode inference experiment type. Use this field to specify a production variant which takes all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant also specify the percentage of requests that Amazon SageMaker replicates.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SourceModelVariantName" : {
          "description" : "The name of the production variant, which takes all the inference requests.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9]([\\-a-zA-Z0-9]*[a-zA-Z0-9])?",
          "maxLength" : 63
        },
        "ShadowModelVariants" : {
          "description" : "List of shadow variant configurations.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 1,
          "items" : {
            "$ref" : "#/definitions/ShadowModelVariantConfig"
          }
        }
      },
      "required" : [ "SourceModelVariantName", "ShadowModelVariants" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "maxLength" : 256,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "required" : [ "Name", "Type", "RoleArn", "EndpointName", "ModelVariants" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:CreateInferenceExperiment", "sagemaker:DescribeInferenceExperiment", "sagemaker:AddTags", "sagemaker:ListTags", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeleteInferenceExperiment", "sagemaker:DescribeInferenceExperiment", "sagemaker:StopInferenceExperiment", "sagemaker:ListTags" ]
    },
    "list" : {
      "permissions" : [ "sagemaker:ListInferenceExperiments" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeInferenceExperiment", "sagemaker:ListTags" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateInferenceExperiment", "sagemaker:StartInferenceExperiment", "sagemaker:StopInferenceExperiment", "sagemaker:DescribeInferenceExperiment", "sagemaker:AddTags", "sagemaker:DeleteTags", "sagemaker:ListTags" ]
    }
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationTime", "/properties/LastModifiedTime", "/properties/EndpointMetadata", "/properties/Status" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Type", "/properties/RoleArn", "/properties/EndpointName", "/properties/KmsKey" ]
}