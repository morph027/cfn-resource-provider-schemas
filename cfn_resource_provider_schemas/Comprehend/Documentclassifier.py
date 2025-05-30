SCHEMA = {
  "typeName" : "AWS::Comprehend::DocumentClassifier",
  "description" : "Document Classifier enables training document classifier models.",
  "additionalProperties" : False,
  "properties" : {
    "DataAccessRoleArn" : {
      "type" : "string",
      "pattern" : "arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "InputDataConfig" : {
      "$ref" : "#/definitions/DocumentClassifierInputDataConfig"
    },
    "OutputDataConfig" : {
      "$ref" : "#/definitions/DocumentClassifierOutputDataConfig"
    },
    "LanguageCode" : {
      "type" : "string",
      "enum" : [ "en", "es", "fr", "it", "de", "pt" ]
    },
    "ModelKmsKeyId" : {
      "$ref" : "#/definitions/KmsKeyId"
    },
    "ModelPolicy" : {
      "type" : "string",
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+",
      "minLength" : 1,
      "maxLength" : 20000
    },
    "DocumentClassifierName" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "Mode" : {
      "type" : "string",
      "enum" : [ "MULTI_CLASS", "MULTI_LABEL" ]
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "insertionOrder" : False,
      "uniqueItems" : True
    },
    "VersionName" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "VolumeKmsKeyId" : {
      "$ref" : "#/definitions/KmsKeyId"
    },
    "VpcConfig" : {
      "$ref" : "#/definitions/VpcConfig"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:document-classifier/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?",
      "minLength" : 1,
      "maxLength" : 256
    }
  },
  "required" : [ "DocumentClassifierName", "DataAccessRoleArn", "InputDataConfig", "LanguageCode" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/DataAccessRoleArn", "/properties/InputDataConfig", "/properties/OutputDataConfig", "/properties/LanguageCode", "/properties/ModelKmsKeyId", "/properties/DocumentClassifierName", "/properties/VersionName", "/properties/Mode", "/properties/VolumeKmsKeyId", "/properties/VpcConfig" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "comprehend:TagResource", "comprehend:UntagResource" ]
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    },
    "DocumentClassifierInputDataConfig" : {
      "type" : "object",
      "properties" : {
        "AugmentedManifests" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AugmentedManifestsListItem"
          },
          "insertionOrder" : False,
          "uniqueItems" : True
        },
        "DataFormat" : {
          "type" : "string",
          "enum" : [ "COMPREHEND_CSV", "AUGMENTED_MANIFEST" ]
        },
        "LabelDelimiter" : {
          "type" : "string",
          "pattern" : "^[ ~!@#$%^*\\-_+=|\\\\:;\\t>?/]$",
          "minLength" : 1,
          "maxLength" : 1
        },
        "DocumentType" : {
          "type" : "string",
          "enum" : [ "PLAIN_TEXT_DOCUMENT", "SEMI_STRUCTURED_DOCUMENT" ]
        },
        "Documents" : {
          "$ref" : "#/definitions/DocumentClassifierDocuments"
        },
        "DocumentReaderConfig" : {
          "$ref" : "#/definitions/DocumentReaderConfig"
        },
        "S3Uri" : {
          "$ref" : "#/definitions/S3Uri"
        },
        "TestS3Uri" : {
          "$ref" : "#/definitions/S3Uri"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    },
    "AugmentedManifestsListItem" : {
      "type" : "object",
      "properties" : {
        "AttributeNames" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*"
          },
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 1,
          "maxItems" : 63
        },
        "S3Uri" : {
          "$ref" : "#/definitions/S3Uri"
        },
        "Split" : {
          "type" : "string",
          "enum" : [ "TRAIN", "TEST" ]
        }
      },
      "required" : [ "AttributeNames", "S3Uri" ],
      "additionalProperties" : False
    },
    "DocumentClassifierDocuments" : {
      "type" : "object",
      "properties" : {
        "S3Uri" : {
          "$ref" : "#/definitions/S3Uri"
        },
        "TestS3Uri" : {
          "$ref" : "#/definitions/S3Uri"
        }
      },
      "required" : [ "S3Uri" ],
      "additionalProperties" : False
    },
    "DocumentReaderConfig" : {
      "type" : "object",
      "properties" : {
        "DocumentReadAction" : {
          "type" : "string",
          "enum" : [ "TEXTRACT_DETECT_DOCUMENT_TEXT", "TEXTRACT_ANALYZE_DOCUMENT" ]
        },
        "DocumentReadMode" : {
          "type" : "string",
          "enum" : [ "SERVICE_DEFAULT", "FORCE_DOCUMENT_READ_ACTION" ]
        },
        "FeatureTypes" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "enum" : [ "TABLES", "FORMS" ]
          },
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 1,
          "maxItems" : 2
        }
      },
      "required" : [ "DocumentReadAction" ],
      "additionalProperties" : False
    },
    "DocumentClassifierOutputDataConfig" : {
      "type" : "object",
      "properties" : {
        "KmsKeyId" : {
          "$ref" : "#/definitions/KmsKeyId"
        },
        "S3Uri" : {
          "$ref" : "#/definitions/S3Uri"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    },
    "VpcConfig" : {
      "type" : "object",
      "properties" : {
        "SecurityGroupIds" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "[-0-9a-zA-Z]+",
            "minLength" : 1,
            "maxLength" : 32
          },
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 1,
          "maxItems" : 5
        },
        "Subnets" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "[-0-9a-zA-Z]+",
            "minLength" : 1,
            "maxLength" : 32
          },
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 1,
          "maxItems" : 16
        }
      },
      "required" : [ "SecurityGroupIds", "Subnets" ],
      "additionalProperties" : False
    },
    "S3Uri" : {
      "type" : "string",
      "pattern" : "s3://[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9](/.*)?",
      "maxLength" : 1024
    },
    "KmsKeyId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "comprehend:CreateDocumentClassifier", "comprehend:DescribeDocumentClassifier", "comprehend:DescribeResourcePolicy", "comprehend:ListTagsForResource", "textract:DetectDocumentText" ],
      "timeoutInMinutes" : 2160
    },
    "read" : {
      "permissions" : [ "comprehend:DescribeDocumentClassifier", "comprehend:DescribeResourcePolicy", "comprehend:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "comprehend:PutResourcePolicy", "comprehend:DeleteResourcePolicy", "comprehend:DescribeResourcePolicy", "comprehend:DescribeDocumentClassifier", "comprehend:ListTagsForResource", "comprehend:TagResource", "comprehend:UntagResource" ],
      "timeoutInMinutes" : 10
    },
    "delete" : {
      "permissions" : [ "comprehend:DescribeDocumentClassifier", "comprehend:DeleteDocumentClassifier" ],
      "timeoutInMinutes" : 120
    },
    "list" : {
      "permissions" : [ "comprehend:ListDocumentClassifiers" ]
    }
  }
}