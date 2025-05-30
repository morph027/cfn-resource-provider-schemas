SCHEMA = {
  "typeName" : "AWS::SageMaker::Pipeline",
  "description" : "Resource Type definition for AWS::SageMaker::Pipeline",
  "additionalProperties" : False,
  "properties" : {
    "PipelineName" : {
      "type" : "string",
      "description" : "The name of the Pipeline.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*"
    },
    "PipelineDisplayName" : {
      "type" : "string",
      "description" : "The display name of the Pipeline.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*"
    },
    "PipelineDescription" : {
      "type" : "string",
      "description" : "The description of the Pipeline.",
      "minLength" : 0,
      "maxLength" : 3072
    },
    "PipelineDefinition" : {
      "type" : "object",
      "oneOf" : [ {
        "additionalProperties" : False,
        "properties" : {
          "PipelineDefinitionBody" : {
            "type" : "string",
            "description" : "A specification that defines the pipeline in JSON format."
          }
        },
        "required" : [ "PipelineDefinitionBody" ]
      }, {
        "additionalProperties" : False,
        "properties" : {
          "PipelineDefinitionS3Location" : {
            "$ref" : "#/definitions/S3Location"
          }
        },
        "required" : [ "PipelineDefinitionS3Location" ]
      } ]
    },
    "RoleArn" : {
      "type" : "string",
      "description" : "Role Arn",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "^arn:aws[a-z\\-]*:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+$"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ParallelismConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaxParallelExecutionSteps" : {
          "description" : "Maximum parallel execution steps",
          "type" : "integer",
          "minimum" : 1
        }
      },
      "required" : [ "MaxParallelExecutionSteps" ]
    }
  },
  "definitions" : {
    "S3Location" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Bucket" : {
          "description" : "The name of the S3 bucket where the PipelineDefinition file is stored.",
          "type" : "string"
        },
        "Key" : {
          "description" : "The file name of the PipelineDefinition file (Amazon S3 object name).",
          "type" : "string"
        },
        "Version" : {
          "description" : "For versioning-enabled buckets, a specific version of the PipelineDefinition file.",
          "type" : "string"
        },
        "ETag" : {
          "description" : "The Amazon S3 ETag (a file checksum) of the PipelineDefinition file. If you don't specify a value, SageMaker skips ETag validation of your PipelineDefinition file.",
          "type" : "string"
        }
      },
      "required" : [ "Bucket", "Key" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "PipelineName", "PipelineDefinition", "RoleArn" ],
  "createOnlyProperties" : [ "/properties/PipelineName" ],
  "primaryIdentifier" : [ "/properties/PipelineName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "sagemaker:AddTags", "sagemaker:ListTags", "sagemaker:DeleteTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "s3:GetObject", "sagemaker:CreatePipeline", "sagemaker:DescribePipeline", "sagemaker:AddTags", "sagemaker:ListTags" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribePipeline", "sagemaker:ListTags" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "s3:GetObject", "sagemaker:UpdatePipeline", "sagemaker:DescribePipeline", "sagemaker:AddTags", "sagemaker:DeleteTags", "sagemaker:ListTags" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeletePipeline" ]
    },
    "list" : {
      "permissions" : [ "sagemaker:ListPipelines" ]
    }
  }
}