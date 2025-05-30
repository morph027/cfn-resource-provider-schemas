SCHEMA = {
  "typeName" : "AWS::Rekognition::StreamProcessor",
  "description" : "The AWS::Rekognition::StreamProcessor type is used to create an Amazon Rekognition StreamProcessor that you can use to analyze streaming videos.\n\n",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Arn" : {
      "description" : "The ARN of the stream processor",
      "type" : "string",
      "maxLength" : 2048
    },
    "KinesisVideoStream" : {
      "description" : "The Kinesis Video Stream that streams the source video.",
      "type" : "object",
      "properties" : {
        "Arn" : {
          "description" : "ARN of the Kinesis Video Stream that streams the source video.",
          "type" : "string",
          "maxLength" : 2048,
          "pattern" : "(^arn:([a-z\\d-]+):kinesisvideo:([a-z\\d-]+):\\d{12}:.+$)"
        }
      },
      "required" : [ "Arn" ],
      "additionalProperties" : False
    },
    "S3Destination" : {
      "description" : "The S3 location in customer's account where inference output & artifacts are stored, as part of connected home feature.",
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "description" : "Name of the S3 bucket.",
          "type" : "string",
          "maxLength" : 63
        },
        "ObjectKeyPrefix" : {
          "description" : "The object key prefix path where the results will be stored. Default is no prefix path",
          "type" : "string",
          "maxLength" : 256
        }
      },
      "required" : [ "BucketName" ],
      "additionalProperties" : False
    },
    "KinesisDataStream" : {
      "description" : "The Amazon Kinesis Data Stream stream to which the Amazon Rekognition stream processor streams the analysis results, as part of face search feature.",
      "type" : "object",
      "properties" : {
        "Arn" : {
          "description" : "ARN of the Kinesis Data Stream stream.",
          "type" : "string",
          "maxLength" : 2048,
          "pattern" : "(^arn:([a-z\\d-]+):kinesis:([a-z\\d-]+):\\d{12}:.+$)"
        }
      },
      "required" : [ "Arn" ],
      "additionalProperties" : False
    },
    "Labels" : {
      "description" : "List of labels that need to be detected in the video stream. Current supported values are PERSON, PET, PACKAGE, ALL.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 1,
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 128
      }
    },
    "ConnectedHomeSettings" : {
      "description" : "Connected home settings to use on a streaming video. Note that either ConnectedHomeSettings or FaceSearchSettings should be set. Not both",
      "type" : "object",
      "properties" : {
        "Labels" : {
          "$ref" : "#/definitions/Labels"
        },
        "MinConfidence" : {
          "description" : "Minimum object class match confidence score that must be met to return a result for a recognized object.",
          "type" : "number",
          "minimum" : 0,
          "maximum" : 100
        }
      },
      "required" : [ "Labels" ],
      "additionalProperties" : False
    },
    "FaceSearchSettings" : {
      "description" : "Face search settings to use on a streaming video. Note that either FaceSearchSettings or ConnectedHomeSettings should be set. Not both",
      "type" : "object",
      "properties" : {
        "CollectionId" : {
          "description" : "The ID of a collection that contains faces that you want to search for.",
          "type" : "string",
          "maxLength" : 255,
          "pattern" : "\\A[a-zA-Z0-9_\\.\\-]+$"
        },
        "FaceMatchThreshold" : {
          "description" : "Minimum face match confidence score percentage that must be met to return a result for a recognized face. The default is 80. 0 is the lowest confidence. 100 is the highest confidence. Values between 0 and 100 are accepted.",
          "type" : "number",
          "minimum" : 0,
          "maximum" : 100
        }
      },
      "required" : [ "CollectionId" ],
      "additionalProperties" : False
    },
    "NotificationChannel" : {
      "description" : "The ARN of the SNS notification channel where events of interests are published, as part of connected home feature.",
      "type" : "object",
      "properties" : {
        "Arn" : {
          "description" : "ARN of the SNS topic.",
          "type" : "string",
          "maxLength" : 2048
        }
      },
      "required" : [ "Arn" ],
      "additionalProperties" : False
    },
    "Point" : {
      "description" : "An (X, Y) cartesian coordinate denoting a point on the frame",
      "type" : "object",
      "properties" : {
        "X" : {
          "description" : "The X coordinate of the point.",
          "type" : "number"
        },
        "Y" : {
          "description" : "The Y coordinate of the point.",
          "type" : "number"
        }
      },
      "required" : [ "X", "Y" ],
      "additionalProperties" : False
    },
    "Polygon" : {
      "description" : "A polygon showing a region of interest. Note that the ordering of the Point entries matter in defining the polygon",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : True,
      "minItems" : 3,
      "items" : {
        "$ref" : "#/definitions/Point"
      }
    },
    "BoundingBox" : {
      "description" : "A bounding box denoting a region of interest in the frame to be analyzed.",
      "type" : "object",
      "properties" : {
        "Height" : {
          "type" : "number",
          "minimum" : 0,
          "maximum" : 100
        },
        "Width" : {
          "type" : "number",
          "minimum" : 0,
          "maximum" : 100
        },
        "Left" : {
          "type" : "number",
          "minimum" : 0,
          "maximum" : 100
        },
        "Top" : {
          "type" : "number",
          "minimum" : 0,
          "maximum" : 100
        }
      },
      "required" : [ "Height", "Width", "Left", "Top" ],
      "additionalProperties" : False
    },
    "DataSharingPreference" : {
      "description" : "Indicates whether Rekognition is allowed to store the video stream data for model-training.",
      "properties" : {
        "OptIn" : {
          "description" : "Flag to enable data-sharing",
          "type" : "boolean"
        }
      },
      "required" : [ "OptIn" ],
      "type" : "object",
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "\\A(?!aws:)[a-zA-Z0-9+\\-=\\._\\:\\/@]+$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256,
          "pattern" : "\\A[a-zA-Z0-9+\\-=\\._\\:\\/@]+$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "Name" : {
      "description" : "Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[a-zA-Z0-9_.\\-]+"
    },
    "KmsKeyId" : {
      "description" : "The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.",
      "type" : "string"
    },
    "RoleArn" : {
      "description" : "ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.",
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "arn:aws(-[\\w]+)*:iam::[0-9]{12}:role/.*"
    },
    "KinesisVideoStream" : {
      "$ref" : "#/definitions/KinesisVideoStream"
    },
    "FaceSearchSettings" : {
      "$ref" : "#/definitions/FaceSearchSettings"
    },
    "ConnectedHomeSettings" : {
      "$ref" : "#/definitions/ConnectedHomeSettings"
    },
    "KinesisDataStream" : {
      "$ref" : "#/definitions/KinesisDataStream"
    },
    "S3Destination" : {
      "$ref" : "#/definitions/S3Destination"
    },
    "NotificationChannel" : {
      "$ref" : "#/definitions/NotificationChannel"
    },
    "DataSharingPreference" : {
      "$ref" : "#/definitions/DataSharingPreference"
    },
    "PolygonRegionsOfInterest" : {
      "description" : "The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "items" : {
        "$ref" : "#/definitions/Polygon"
      }
    },
    "BoundingBoxRegionsOfInterest" : {
      "description" : "The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "items" : {
        "$ref" : "#/definitions/BoundingBox"
      }
    },
    "Status" : {
      "description" : "Current status of the stream processor.",
      "type" : "string"
    },
    "StatusMessage" : {
      "description" : "Detailed status message about the stream processor.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : False,
    "permissions" : [ "rekognition:TagResource", "rekognition:UntagResource", "rekognition:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "RoleArn", "KinesisVideoStream" ],
  "oneOf" : [ {
    "required" : [ "ConnectedHomeSettings", "S3Destination", "NotificationChannel" ]
  }, {
    "required" : [ "FaceSearchSettings", "KinesisDataStream" ]
  } ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Status", "/properties/StatusMessage" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/KmsKeyId", "/properties/RoleArn", "/properties/KinesisVideoStream", "/properties/ConnectedHomeSettings", "/properties/FaceSearchSettings", "/properties/KinesisDataStream", "/properties/S3Destination", "/properties/NotificationChannel", "/properties/BoundingBoxRegionsOfInterest", "/properties/PolygonRegionsOfInterest", "/properties/DataSharingPreference" ],
  "$comment" : "We explicitly specify the replacement strategy to be delete_then_create because we cannot create a new SP resource with the same name or same KVS input before deleting the old one",
  "replacementStrategy" : "delete_then_create",
  "handlers" : {
    "create" : {
      "permissions" : [ "rekognition:CreateStreamProcessor", "iam:PassRole", "rekognition:DescribeStreamProcessor", "rekognition:ListTagsForResource", "rekognition:TagResource" ]
    },
    "read" : {
      "permissions" : [ "rekognition:DescribeStreamProcessor", "rekognition:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "rekognition:TagResource", "rekognition:UntagResource", "rekognition:ListTagsForResource", "rekognition:DescribeStreamProcessor" ]
    },
    "delete" : {
      "permissions" : [ "rekognition:DeleteStreamProcessor" ]
    },
    "list" : {
      "permissions" : [ "rekognition:ListStreamProcessors" ]
    }
  }
}