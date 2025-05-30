SCHEMA = {
  "typeName" : "AWS::SageMaker::ModelCard",
  "description" : "Resource Type definition for AWS::SageMaker::ModelCard.",
  "additionalProperties" : False,
  "properties" : {
    "ModelCardArn" : {
      "description" : "The Amazon Resource Name (ARN) of the successfully created model card.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "^arn:aws[a-z\\-]*:sagemaker:[a-z0-9\\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$"
    },
    "ModelCardVersion" : {
      "description" : "A version of the model card.",
      "type" : "integer",
      "minimum" : 1
    },
    "ModelCardName" : {
      "description" : "The unique name of the model card.",
      "type" : "string",
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$"
    },
    "SecurityConfig" : {
      "$ref" : "#/definitions/SecurityConfig"
    },
    "ModelCardStatus" : {
      "description" : "The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.",
      "type" : "string",
      "enum" : [ "Draft", "PendingReview", "Approved", "Archived" ]
    },
    "Content" : {
      "$ref" : "#/definitions/Content"
    },
    "CreationTime" : {
      "description" : "The date and time the model card was created.",
      "type" : "string"
    },
    "CreatedBy" : {
      "description" : "Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.",
      "$ref" : "#/definitions/UserContext"
    },
    "LastModifiedTime" : {
      "description" : "The date and time the model card was last modified.",
      "type" : "string"
    },
    "LastModifiedBy" : {
      "description" : "Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.",
      "$ref" : "#/definitions/UserContext"
    },
    "ModelCardProcessingStatus" : {
      "description" : "The processing status of model card deletion. The ModelCardProcessingStatus updates throughout the different deletion steps.",
      "type" : "string",
      "default" : "UnsetValue",
      "enum" : [ "UnsetValue", "DeleteInProgress", "DeletePending", "ContentDeleted", "ExportJobsDeleted", "DeleteCompleted", "DeleteFailed" ]
    },
    "Tags" : {
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 50,
      "description" : "Key-value pairs used to manage metadata for model cards.",
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "SecurityConfig" : {
      "type" : "object",
      "description" : "An optional Key Management Service key to encrypt, decrypt, and re-encrypt model card content for regulated workloads with highly sensitive data.\n\n",
      "additionalProperties" : False,
      "properties" : {
        "KmsKeyId" : {
          "type" : "string",
          "description" : "A Key Management Service key ID to use for encrypting a model card.",
          "maxLength" : 2048,
          "pattern" : ".*"
        }
      }
    },
    "UserContext" : {
      "description" : "Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "UserProfileArn" : {
          "description" : "The Amazon Resource Name (ARN) of the user's profile.",
          "type" : "string",
          "default" : "UnsetValue"
        },
        "UserProfileName" : {
          "description" : "The name of the user's profile.",
          "type" : "string",
          "default" : "UnsetValue"
        },
        "DomainId" : {
          "description" : "The domain associated with the user.",
          "type" : "string",
          "default" : "UnsetValue"
        }
      }
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag key. Tag keys must be unique per resource.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag value.",
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "Content" : {
      "type" : "object",
      "description" : "The content of the model card.",
      "additionalProperties" : False,
      "properties" : {
        "ModelOverview" : {
          "$ref" : "#/definitions/ModelOverview"
        },
        "ModelPackageDetails" : {
          "$ref" : "#/definitions/ModelPackageDetails"
        },
        "IntendedUses" : {
          "$ref" : "#/definitions/IntendedUses"
        },
        "BusinessDetails" : {
          "$ref" : "#/definitions/BusinessDetails"
        },
        "TrainingDetails" : {
          "$ref" : "#/definitions/TrainingDetails"
        },
        "EvaluationDetails" : {
          "$ref" : "#/definitions/EvaluationDetails"
        },
        "AdditionalInformation" : {
          "$ref" : "#/definitions/AdditionalInformation"
        }
      }
    },
    "ModelOverview" : {
      "type" : "object",
      "description" : "Overview about the model.",
      "additionalProperties" : False,
      "properties" : {
        "ModelDescription" : {
          "description" : "description of model.",
          "type" : "string",
          "maxLength" : 1024
        },
        "ModelOwner" : {
          "description" : "Owner of model.",
          "type" : "string",
          "maxLength" : 1024
        },
        "ModelCreator" : {
          "description" : "Creator of model.",
          "type" : "string",
          "maxLength" : 1024
        },
        "ProblemType" : {
          "description" : "Problem being solved with the model.",
          "type" : "string",
          "maxLength" : 1024
        },
        "AlgorithmType" : {
          "description" : "Algorithm used to solve the problem.",
          "type" : "string",
          "maxLength" : 1024
        },
        "ModelId" : {
          "description" : "SageMaker Model Arn or Non SageMaker Model id.",
          "type" : "string",
          "maxLength" : 1024
        },
        "ModelArtifact" : {
          "description" : "Location of the model artifact.",
          "type" : "array",
          "insertionOrder" : True,
          "maxItems" : 15,
          "items" : {
            "type" : "string",
            "maxLength" : 1024
          }
        },
        "ModelName" : {
          "description" : "Name of the model.",
          "type" : "string",
          "maxLength" : 1024
        },
        "ModelVersion" : {
          "description" : "Version of the model.",
          "type" : "number",
          "minimum" : 1
        },
        "InferenceEnvironment" : {
          "description" : "Overview about the inference.",
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "ContainerImage" : {
              "description" : "SageMaker inference image uri.",
              "type" : "array",
              "insertionOrder" : True,
              "maxItems" : 15,
              "items" : {
                "type" : "string",
                "maxLength" : 1024
              }
            }
          }
        }
      }
    },
    "ModelPackageDetails" : {
      "description" : "Metadata information related to model package version",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ModelPackageDescription" : {
          "description" : "A brief summary of the model package",
          "type" : "string",
          "maxLength" : 1024
        },
        "ModelPackageArn" : {
          "description" : "The Amazon Resource Name (ARN) of the model package",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "CreatedBy" : {
          "description" : "Information about the user who created model package.",
          "$ref" : "#/definitions/ModelPackageCreator"
        },
        "ModelPackageStatus" : {
          "description" : "Current status of model package",
          "type" : "string",
          "enum" : [ "Pending", "InProgress", "Completed", "Failed", "Deleting" ]
        },
        "ModelApprovalStatus" : {
          "description" : "Current approval status of model package",
          "type" : "string",
          "enum" : [ "Approved", "Rejected", "PendingManualApproval" ]
        },
        "ApprovalDescription" : {
          "description" : "A description provided for the model approval",
          "type" : "string",
          "maxLength" : 1024
        },
        "ModelPackageGroupName" : {
          "description" : "If the model is a versioned model, the name of the model group that the versioned model belongs to.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 63
        },
        "ModelPackageName" : {
          "description" : "Name of the model package",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 63
        },
        "ModelPackageVersion" : {
          "description" : "Version of the model package",
          "type" : "number",
          "minimum" : 1.0
        },
        "Domain" : {
          "description" : "The machine learning domain of the model package you specified. Common machine learning domains include computer vision and natural language processing.",
          "type" : "string"
        },
        "Task" : {
          "description" : "The machine learning task you specified that your model package accomplishes. Common machine learning tasks include object detection and image classification.",
          "type" : "string"
        },
        "SourceAlgorithms" : {
          "description" : "A list of algorithms that were used to create a model package.",
          "$ref" : "#/definitions/SourceAlgorithms"
        },
        "InferenceSpecification" : {
          "description" : "Details about inference jobs that can be run with models based on this model package.",
          "$ref" : "#/definitions/InferenceSpecification"
        }
      }
    },
    "IntendedUses" : {
      "description" : "Intended usage of model.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PurposeOfModel" : {
          "description" : "Why the model was developed?",
          "type" : "string",
          "maxLength" : 2048
        },
        "IntendedUses" : {
          "description" : "intended use cases.",
          "type" : "string",
          "maxLength" : 2048
        },
        "FactorsAffectingModelEfficiency" : {
          "type" : "string",
          "maxLength" : 2048
        },
        "RiskRating" : {
          "$ref" : "#/definitions/RiskRating"
        },
        "ExplanationsForRiskRating" : {
          "type" : "string",
          "maxLength" : 2048
        }
      }
    },
    "BusinessDetails" : {
      "description" : "Business details.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BusinessProblem" : {
          "type" : "string",
          "description" : "What business problem does the model solve?",
          "maxLength" : 2048
        },
        "BusinessStakeholders" : {
          "type" : "string",
          "description" : "Business stakeholders.",
          "maxLength" : 2048
        },
        "LineOfBusiness" : {
          "type" : "string",
          "description" : "Line of business.",
          "maxLength" : 2048
        }
      }
    },
    "TrainingDetails" : {
      "description" : "Overview about the training.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ObjectiveFunction" : {
          "$ref" : "#/definitions/ObjectiveFunction"
        },
        "TrainingObservations" : {
          "type" : "string",
          "maxLength" : 1024
        },
        "TrainingJobDetails" : {
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "TrainingArn" : {
              "description" : "SageMaker Training job arn.",
              "type" : "string",
              "maxLength" : 1024
            },
            "TrainingDatasets" : {
              "description" : "Location of the model datasets.",
              "type" : "array",
              "insertionOrder" : True,
              "maxItems" : 15,
              "items" : {
                "type" : "string",
                "maxLength" : 1024
              }
            },
            "TrainingEnvironment" : {
              "type" : "object",
              "additionalProperties" : False,
              "properties" : {
                "ContainerImage" : {
                  "description" : "SageMaker training image uri.",
                  "type" : "array",
                  "insertionOrder" : True,
                  "maxItems" : 15,
                  "items" : {
                    "type" : "string",
                    "maxLength" : 1024
                  }
                }
              }
            },
            "TrainingMetrics" : {
              "type" : "array",
              "insertionOrder" : True,
              "items" : {
                "maxItems" : 50,
                "$ref" : "#/definitions/TrainingMetric"
              }
            },
            "UserProvidedTrainingMetrics" : {
              "type" : "array",
              "insertionOrder" : True,
              "items" : {
                "maxItems" : 50,
                "$ref" : "#/definitions/TrainingMetric"
              }
            },
            "HyperParameters" : {
              "type" : "array",
              "insertionOrder" : True,
              "items" : {
                "maxItems" : 100,
                "$ref" : "#/definitions/TrainingHyperParameter"
              }
            },
            "UserProvidedHyperParameters" : {
              "type" : "array",
              "insertionOrder" : True,
              "items" : {
                "maxItems" : 100,
                "$ref" : "#/definitions/TrainingHyperParameter"
              }
            }
          }
        }
      }
    },
    "EvaluationDetails" : {
      "type" : "array",
      "default" : [ ],
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/EvaluationDetail"
      }
    },
    "EvaluationDetail" : {
      "description" : "item of evaluation details",
      "type" : "object",
      "required" : [ "Name" ],
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,63}"
        },
        "EvaluationObservation" : {
          "type" : "string",
          "maxLength" : 2096
        },
        "EvaluationJobArn" : {
          "type" : "string",
          "maxLength" : 256
        },
        "Datasets" : {
          "type" : "array",
          "insertionOrder" : True,
          "items" : {
            "type" : "string",
            "maxLength" : 1024
          },
          "maxItems" : 10
        },
        "Metadata" : {
          "description" : "additional attributes associated with the evaluation results.",
          "type" : "object",
          "additionalProperties" : False,
          "patternProperties" : {
            "[a-zA-Z_][a-zA-Z0-9_]*" : {
              "type" : "string",
              "maxLength" : 1024
            }
          }
        },
        "MetricGroups" : {
          "type" : "array",
          "insertionOrder" : True,
          "default" : [ ],
          "items" : {
            "$ref" : "#/definitions/MetricGroup"
          }
        }
      }
    },
    "MetricGroup" : {
      "type" : "object",
      "description" : "item in metric groups",
      "additionalProperties" : False,
      "required" : [ "Name", "MetricData" ],
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,63}"
        },
        "MetricData" : {
          "type" : "array",
          "insertionOrder" : True,
          "items" : {
            "anyOf" : [ {
              "$ref" : "#/definitions/SimpleMetric"
            }, {
              "$ref" : "#/definitions/LinearGraphMetric"
            }, {
              "$ref" : "#/definitions/BarChartMetric"
            }, {
              "$ref" : "#/definitions/MatrixMetric"
            } ]
          }
        }
      }
    },
    "AdditionalInformation" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EthicalConsiderations" : {
          "description" : "Any ethical considerations that the author wants to provide.",
          "type" : "string",
          "maxLength" : 2048
        },
        "CaveatsAndRecommendations" : {
          "description" : "Caveats and recommendations for people who might use this model in their applications.",
          "type" : "string",
          "maxLength" : 2048
        },
        "CustomDetails" : {
          "type" : "object",
          "description" : "customer details.",
          "additionalProperties" : False,
          "patternProperties" : {
            "[a-zA-Z_][a-zA-Z0-9_]*" : {
              "type" : "string",
              "maxLength" : 1024
            }
          }
        }
      }
    },
    "ModelPackageCreator" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "UserProfileName" : {
          "description" : "The name of the user's profile in Studio",
          "type" : "string",
          "maxLength" : 63
        }
      }
    },
    "SourceAlgorithms" : {
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 1,
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/SourceAlgorithm"
      }
    },
    "SourceAlgorithm" : {
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "AlgorithmName" ],
      "properties" : {
        "AlgorithmName" : {
          "description" : "The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.",
          "type" : "string",
          "maxLength" : 170
        },
        "ModelDataUrl" : {
          "description" : "The Amazon S3 path where the model artifacts, which result from model training, are stored.",
          "type" : "string",
          "maxLength" : 1024
        }
      }
    },
    "InferenceSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "Containers" ],
      "properties" : {
        "Containers" : {
          "description" : "Contains inference related information which were used to create model package.",
          "type" : "array",
          "insertionOrder" : True,
          "minItems" : 1,
          "maxItems" : 15,
          "items" : {
            "$ref" : "#/definitions/Container"
          }
        }
      }
    },
    "Container" : {
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "Image" ],
      "properties" : {
        "ModelDataUrl" : {
          "description" : "The Amazon S3 path where the model artifacts, which result from model training, are stored.",
          "type" : "string",
          "maxLength" : 1024
        },
        "Image" : {
          "description" : "Inference environment path. The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.",
          "type" : "string",
          "maxLength" : 255
        },
        "NearestModelName" : {
          "description" : "The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model.",
          "type" : "string"
        }
      }
    },
    "RiskRating" : {
      "description" : "Risk rating of model.",
      "type" : "string",
      "enum" : [ "High", "Medium", "Low", "Unknown" ]
    },
    "ObjectiveFunction" : {
      "description" : "the objective function the model will optimize for.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Function" : {
          "description" : "objective function that training job is optimized for.",
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "Function" : {
              "type" : "string",
              "enum" : [ "Maximize", "Minimize" ]
            },
            "Facet" : {
              "type" : "string",
              "maxLength" : 63
            },
            "Condition" : {
              "type" : "string",
              "maxLength" : 63
            }
          }
        },
        "Notes" : {
          "type" : "string",
          "maxLength" : 1024
        }
      }
    },
    "TrainingMetric" : {
      "description" : "training metric data.",
      "type" : "object",
      "required" : [ "Name", "Value" ],
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,255}"
        },
        "Notes" : {
          "type" : "string",
          "maxLength" : 1024
        },
        "Value" : {
          "type" : "number"
        }
      }
    },
    "TrainingHyperParameter" : {
      "description" : "training hyper parameter",
      "type" : "object",
      "required" : [ "Name", "Value" ],
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,255}"
        },
        "Value" : {
          "type" : "string",
          "pattern" : ".{1,255}"
        }
      }
    },
    "LinearGraphMetric" : {
      "description" : "Linear graph metric.",
      "type" : "object",
      "required" : [ "Name", "Type", "Value" ],
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,255}"
        },
        "Notes" : {
          "type" : "string",
          "maxLength" : 1024
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "linear_graph" ]
        },
        "Value" : {
          "anyOf" : [ {
            "type" : "array",
            "insertionOrder" : True,
            "items" : {
              "type" : "array",
              "insertionOrder" : True,
              "items" : {
                "type" : "number"
              },
              "minItems" : 2,
              "maxItems" : 2
            },
            "minItems" : 1
          } ]
        },
        "XAxisName" : {
          "$ref" : "#/definitions/AxisNameString"
        },
        "YAxisName" : {
          "$ref" : "#/definitions/AxisNameString"
        }
      }
    },
    "BarChartMetric" : {
      "type" : "object",
      "required" : [ "Name", "Type", "Value" ],
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,255}"
        },
        "Notes" : {
          "type" : "string",
          "maxLength" : 1024
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "bar_chart" ]
        },
        "Value" : {
          "anyOf" : [ {
            "type" : "array",
            "insertionOrder" : True,
            "items" : {
              "type" : "number"
            },
            "minItems" : 1
          } ]
        },
        "XAxisName" : {
          "$ref" : "#/definitions/AxisNameArray"
        },
        "YAxisName" : {
          "$ref" : "#/definitions/AxisNameString"
        }
      }
    },
    "MatrixMetric" : {
      "type" : "object",
      "required" : [ "Name", "Type", "Value" ],
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,255}"
        },
        "Notes" : {
          "type" : "string",
          "maxLength" : 1024
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "matrix" ]
        },
        "Value" : {
          "anyOf" : [ {
            "type" : "array",
            "insertionOrder" : True,
            "items" : {
              "type" : "array",
              "insertionOrder" : True,
              "items" : {
                "type" : "number"
              },
              "minItems" : 1,
              "maxItems" : 20
            },
            "minItems" : 1,
            "maxItems" : 20
          } ]
        },
        "XAxisName" : {
          "$ref" : "#/definitions/AxisNameArray"
        },
        "YAxisName" : {
          "$ref" : "#/definitions/AxisNameArray"
        }
      }
    },
    "SimpleMetric" : {
      "description" : "metric data",
      "type" : "object",
      "required" : [ "Name", "Type", "Value" ],
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : ".{1,255}"
        },
        "Notes" : {
          "type" : "string",
          "maxLength" : 1024
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "number", "string", "boolean" ]
        },
        "Value" : {
          "anyOf" : [ {
            "type" : "number"
          }, {
            "type" : "string",
            "maxLength" : 63
          }, {
            "type" : "boolean"
          } ]
        },
        "XAxisName" : {
          "$ref" : "#/definitions/AxisNameString"
        },
        "YAxisName" : {
          "$ref" : "#/definitions/AxisNameString"
        }
      }
    },
    "AxisNameString" : {
      "type" : "string",
      "maxLength" : 63
    },
    "AxisNameArray" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "type" : "string",
        "maxLength" : 63
      }
    }
  },
  "required" : [ "ModelCardName", "Content", "ModelCardStatus" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "sagemaker:AddTags", "sagemaker:ListTags", "sagemaker:DeleteTags" ]
  },
  "readOnlyProperties" : [ "/properties/ModelCardArn", "/properties/ModelCardVersion", "/properties/CreatedBy/DomainId", "/properties/CreatedBy/UserProfileArn", "/properties/CreatedBy/UserProfileName", "/properties/LastModifiedBy/DomainId", "/properties/LastModifiedBy/UserProfileArn", "/properties/LastModifiedBy/UserProfileName", "/properties/CreationTime", "/properties/LastModifiedTime", "/properties/ModelCardProcessingStatus" ],
  "primaryIdentifier" : [ "/properties/ModelCardName" ],
  "createOnlyProperties" : [ "/properties/ModelCardName", "/properties/SecurityConfig" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:CreateModelCard", "sagemaker:DescribeModel", "kms:DescribeKey", "kms:GenerateDataKey", "kms:CreateGrant", "sagemaker:DescribeModelPackageGroup", "sagemaker:DescribeModelPackage", "sagemaker:AddTags" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeModelCard", "sagemaker:DescribeModelPackageGroup", "sagemaker:DescribeModelPackage", "kms:Decrypt", "sagemaker:ListTags" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateModelCard", "sagemaker:DescribeModelCard", "sagemaker:DescribeModel", "kms:GenerateDataKey", "kms:Decrypt", "sagemaker:DescribeModelPackageGroup", "sagemaker:DescribeModelPackage", "sagemaker:ListTags", "sagemaker:AddTags", "sagemaker:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DescribeModelCard", "sagemaker:DeleteModelCard", "sagemaker:DescribeModelPackageGroup", "sagemaker:DescribeModelPackage", "kms:RetireGrant", "kms:Decrypt", "sagemaker:ListTags", "sagemaker:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "sagemaker:ListModelCards", "sagemaker:ListModelCardVersions" ]
    }
  }
}