SCHEMA = {
  "typeName" : "AWS::SageMaker::ImageVersion",
  "description" : "Resource Type definition for AWS::SageMaker::ImageVersion",
  "additionalProperties" : False,
  "properties" : {
    "ImageName" : {
      "$ref" : "#/definitions/ImageName"
    },
    "ImageArn" : {
      "$ref" : "#/definitions/ImageArn"
    },
    "ImageVersionArn" : {
      "$ref" : "#/definitions/ImageVersionArn"
    },
    "BaseImage" : {
      "$ref" : "#/definitions/BaseImage"
    },
    "ContainerImage" : {
      "$ref" : "#/definitions/ContainerImage"
    },
    "Version" : {
      "$ref" : "#/definitions/Version"
    },
    "Alias" : {
      "$ref" : "#/definitions/Alias"
    },
    "Aliases" : {
      "$ref" : "#/definitions/Aliases"
    },
    "VendorGuidance" : {
      "$ref" : "#/definitions/VendorGuidance"
    },
    "JobType" : {
      "$ref" : "#/definitions/JobType"
    },
    "MLFramework" : {
      "$ref" : "#/definitions/MLFramework"
    },
    "ProgrammingLang" : {
      "$ref" : "#/definitions/ProgrammingLang"
    },
    "Processor" : {
      "$ref" : "#/definitions/Processor"
    },
    "Horovod" : {
      "$ref" : "#/definitions/Horovod"
    },
    "ReleaseNotes" : {
      "$ref" : "#/definitions/ReleaseNotes"
    }
  },
  "definitions" : {
    "ImageName" : {
      "type" : "string",
      "description" : "The name of the image this version belongs to.",
      "pattern" : "^[A-Za-z0-9]([-.]?[A-Za-z0-9])*$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "ImageArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the parent image.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^arn:aws(-[\\w]+)*:sagemaker:[a-z0-9\\-]*:[0-9]{12}:image\\/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*$"
    },
    "ImageVersionArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the image version.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^arn:aws(-[\\w]+)*:sagemaker:[a-z0-9\\-]*:[0-9]{12}:image-version\\/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*\\/[0-9]+$"
    },
    "BaseImage" : {
      "type" : "string",
      "description" : "The registry path of the container image on which this image version is based.",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : ".+"
    },
    "ContainerImage" : {
      "type" : "string",
      "description" : "The registry path of the container image that contains this image version.",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : ".+"
    },
    "Alias" : {
      "type" : "string",
      "description" : "The alias of the image version.",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "(?!^[.-])^([a-zA-Z0-9-_.]+)$"
    },
    "Aliases" : {
      "type" : "array",
      "description" : "List of aliases for the image version.",
      "items" : {
        "$ref" : "#/definitions/Alias"
      }
    },
    "Version" : {
      "type" : "integer",
      "description" : "The version number of the image version.",
      "minimum" : 1
    },
    "VendorGuidance" : {
      "type" : "string",
      "description" : "The availability of the image version specified by the maintainer.",
      "enum" : [ "NOT_PROVIDED", "STABLE", "TO_BE_ARCHIVED", "ARCHIVED" ]
    },
    "JobType" : {
      "type" : "string",
      "description" : "Indicates SageMaker job type compatibility.",
      "enum" : [ "TRAINING", "INFERENCE", "NOTEBOOK_KERNEL" ]
    },
    "MLFramework" : {
      "type" : "string",
      "description" : "The machine learning framework vended in the image version.",
      "pattern" : "^[a-zA-Z]+ ?\\d+\\.\\d+(\\.\\d+)?$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "ProgrammingLang" : {
      "type" : "string",
      "description" : "The supported programming language and its version.",
      "pattern" : "^[a-zA-Z]+ ?\\d+\\.\\d+(\\.\\d+)?$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Processor" : {
      "type" : "string",
      "description" : "Indicates CPU or GPU compatibility.",
      "enum" : [ "CPU", "GPU" ]
    },
    "Horovod" : {
      "type" : "boolean",
      "description" : "Indicates Horovod compatibility."
    },
    "ReleaseNotes" : {
      "type" : "string",
      "description" : "The maintainer description of the image version.",
      "pattern" : ".*",
      "minLength" : 1,
      "maxLength" : 255
    }
  },
  "required" : [ "ImageName", "BaseImage" ],
  "primaryIdentifier" : [ "/properties/ImageVersionArn" ],
  "readOnlyProperties" : [ "/properties/ImageVersionArn", "/properties/ImageArn", "/properties/Version", "/properties/ContainerImage" ],
  "createOnlyProperties" : [ "/properties/ImageName", "/properties/BaseImage" ],
  "writeOnlyProperties" : [ "/properties/Aliases", "/properties/Alias" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:CreateImageVersion", "sagemaker:DescribeImageVersion" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeImageVersion" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateImageVersion", "sagemaker:DescribeImageVersion", "sagemaker:ListAliases" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeleteImageVersion", "sagemaker:DescribeImageVersion" ]
    },
    "list" : {
      "permissions" : [ "sagemaker:ListImageVersions" ],
      "handlerSchema" : {
        "properties" : {
          "ImageName" : {
            "$ref" : "resource-schema.json#/properties/ImageName"
          }
        },
        "required" : [ "ImageName" ]
      }
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sagemaker"
}