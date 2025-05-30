SCHEMA = {
  "typeName" : "AWS::Transfer::Workflow",
  "description" : "Resource Type definition for AWS::Transfer::Workflow",
  "definitions" : {
    "S3Tag" : {
      "description" : "Specifies the key-value pair that are assigned to a file during the execution of a Tagging step.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "The name assigned to the tag that you create.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "The value that corresponds to the key.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "EfsInputFileLocation" : {
      "description" : "Specifies the details for an EFS file.",
      "type" : "object",
      "properties" : {
        "FileSystemId" : {
          "description" : "Specifies the EFS filesystem that contains the file.",
          "type" : "string",
          "pattern" : "^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})$",
          "minLength" : 0,
          "maxLength" : 128
        },
        "Path" : {
          "description" : "The name assigned to the file when it was created in EFS. You use the object path to retrieve the object.",
          "type" : "string",
          "pattern" : "^[^\\x00]+$",
          "minLength" : 1,
          "maxLength" : 65536
        }
      },
      "additionalProperties" : False
    },
    "S3InputFileLocation" : {
      "description" : "Specifies the details for a S3 file.",
      "type" : "object",
      "properties" : {
        "Bucket" : {
          "description" : "Specifies the S3 bucket that contains the file.",
          "type" : "string",
          "pattern" : "^[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9]$",
          "minLength" : 3,
          "maxLength" : 63
        },
        "Key" : {
          "description" : "The name assigned to the file when it was created in S3. You use the object key to retrieve the object.",
          "type" : "string",
          "pattern" : ".*",
          "minLength" : 0,
          "maxLength" : 1024
        }
      },
      "additionalProperties" : False
    },
    "InputFileLocation" : {
      "description" : "Specifies the location for the file being decrypted. Only applicable for the Decrypt type of workflow steps.",
      "type" : "object",
      "properties" : {
        "S3FileLocation" : {
          "$ref" : "#/definitions/S3InputFileLocation"
        },
        "EfsFileLocation" : {
          "$ref" : "#/definitions/EfsInputFileLocation"
        }
      },
      "additionalProperties" : False
    },
    "S3FileLocation" : {
      "description" : "Specifies the location for the file being copied. Only applicable for the Copy type of workflow steps.",
      "type" : "object",
      "properties" : {
        "S3FileLocation" : {
          "$ref" : "#/definitions/S3InputFileLocation"
        }
      },
      "additionalProperties" : False
    },
    "WorkflowStep" : {
      "description" : "The basic building block of a workflow.",
      "type" : "object",
      "properties" : {
        "CopyStepDetails" : {
          "description" : "Details for a step that performs a file copy.",
          "type" : "object",
          "properties" : {
            "DestinationFileLocation" : {
              "$ref" : "#/definitions/S3FileLocation"
            },
            "Name" : {
              "description" : "The name of the step, used as an identifier.",
              "type" : "string",
              "pattern" : "^[\\w-]*$",
              "minLength" : 0,
              "maxLength" : 30
            },
            "OverwriteExisting" : {
              "description" : "A flag that indicates whether or not to overwrite an existing file of the same name. The default is FALSE.",
              "type" : "string",
              "enum" : [ "TRUE", "FALSE" ]
            },
            "SourceFileLocation" : {
              "description" : "Specifies which file to use as input to the workflow step.",
              "type" : "string",
              "pattern" : "^\\$\\{(\\w+.)+\\w+\\}$",
              "minLength" : 0,
              "maxLength" : 256
            }
          },
          "additionalProperties" : False
        },
        "CustomStepDetails" : {
          "description" : "Details for a step that invokes a lambda function.",
          "type" : "object",
          "properties" : {
            "Name" : {
              "description" : "The name of the step, used as an identifier.",
              "type" : "string",
              "pattern" : "^[\\w-]*$",
              "minLength" : 0,
              "maxLength" : 30
            },
            "Target" : {
              "description" : "The ARN for the lambda function that is being called.",
              "type" : "string",
              "pattern" : "arn:[a-z-]+:lambda:.*$",
              "minLength" : 0,
              "maxLength" : 170
            },
            "TimeoutSeconds" : {
              "description" : "Timeout, in seconds, for the step.",
              "type" : "integer",
              "minimum" : 1,
              "maximum" : 1800
            },
            "SourceFileLocation" : {
              "description" : "Specifies which file to use as input to the workflow step.",
              "type" : "string",
              "pattern" : "^\\$\\{(\\w+.)+\\w+\\}$",
              "minLength" : 0,
              "maxLength" : 256
            }
          },
          "additionalProperties" : False
        },
        "DecryptStepDetails" : {
          "description" : "Details for a step that performs a file decryption.",
          "type" : "object",
          "properties" : {
            "DestinationFileLocation" : {
              "$ref" : "#/definitions/InputFileLocation"
            },
            "Name" : {
              "description" : "The name of the step, used as an identifier.",
              "type" : "string",
              "pattern" : "^[\\w-]*$",
              "minLength" : 0,
              "maxLength" : 30
            },
            "Type" : {
              "description" : "Specifies which encryption method to use.",
              "type" : "string",
              "enum" : [ "PGP" ]
            },
            "OverwriteExisting" : {
              "description" : "A flag that indicates whether or not to overwrite an existing file of the same name. The default is FALSE.",
              "type" : "string",
              "enum" : [ "TRUE", "FALSE" ]
            },
            "SourceFileLocation" : {
              "description" : "Specifies which file to use as input to the workflow step.",
              "type" : "string",
              "pattern" : "^\\$\\{(\\w+.)+\\w+\\}$",
              "minLength" : 0,
              "maxLength" : 256
            }
          },
          "required" : [ "DestinationFileLocation", "Type" ],
          "additionalProperties" : False
        },
        "DeleteStepDetails" : {
          "description" : "Details for a step that deletes the file.",
          "type" : "object",
          "properties" : {
            "Name" : {
              "description" : "The name of the step, used as an identifier.",
              "type" : "string",
              "pattern" : "^[\\w-]*$",
              "minLength" : 0,
              "maxLength" : 30
            },
            "SourceFileLocation" : {
              "description" : "Specifies which file to use as input to the workflow step.",
              "type" : "string",
              "pattern" : "^\\$\\{(\\w+.)+\\w+\\}$",
              "minLength" : 0,
              "maxLength" : 256
            }
          },
          "additionalProperties" : False
        },
        "TagStepDetails" : {
          "description" : "Details for a step that creates one or more tags.",
          "type" : "object",
          "properties" : {
            "Name" : {
              "description" : "The name of the step, used as an identifier.",
              "type" : "string",
              "pattern" : "^[\\w-]*$",
              "minLength" : 0,
              "maxLength" : 30
            },
            "Tags" : {
              "description" : "Array that contains from 1 to 10 key/value pairs.",
              "type" : "array",
              "maxItems" : 10,
              "uniqueItems" : True,
              "insertionOrder" : False,
              "items" : {
                "$ref" : "#/definitions/S3Tag"
              }
            },
            "SourceFileLocation" : {
              "description" : "Specifies which file to use as input to the workflow step.",
              "type" : "string",
              "pattern" : "^\\$\\{(\\w+.)+\\w+\\}$",
              "minLength" : 0,
              "maxLength" : 256
            }
          },
          "additionalProperties" : False
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "COPY", "CUSTOM", "DECRYPT", "DELETE", "TAG" ]
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "Creates a key-value pair for a specific resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The name assigned to the tag that you create.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "Contains one or more values that you assigned to the key name you create.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "OnExceptionSteps" : {
      "description" : "Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.",
      "type" : "array",
      "maxItems" : 8,
      "uniqueItems" : True,
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/WorkflowStep"
      }
    },
    "Steps" : {
      "description" : "Specifies the details for the steps that are in the specified workflow.",
      "type" : "array",
      "maxItems" : 8,
      "uniqueItems" : True,
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/WorkflowStep"
      }
    },
    "Tags" : {
      "description" : "Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Description" : {
      "description" : "A textual description for the workflow.",
      "type" : "string",
      "pattern" : "^[\\w\\- ]*$",
      "minLength" : 0,
      "maxLength" : 256
    },
    "WorkflowId" : {
      "description" : "A unique identifier for the workflow.",
      "type" : "string",
      "pattern" : "^w-([a-z0-9]{17})$",
      "minLength" : 19,
      "maxLength" : 19
    },
    "Arn" : {
      "description" : "Specifies the unique Amazon Resource Name (ARN) for the workflow.",
      "type" : "string",
      "pattern" : "arn:.*",
      "minLength" : 20,
      "maxLength" : 1600
    }
  },
  "required" : [ "Steps" ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/WorkflowId", "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Steps", "/properties/OnExceptionSteps", "/properties/Description" ],
  "primaryIdentifier" : [ "/properties/WorkflowId" ],
  "tagging" : {
    "cloudFormationSystemTags" : True,
    "tagOnCreate" : True,
    "tagProperty" : "/properties/Tags",
    "tagUpdatable" : True,
    "taggable" : True,
    "permissions" : [ "transfer:ListTagsForResource", "transfer:UnTagResource", "transfer:TagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "transfer:CreateWorkflow", "transfer:TagResource" ]
    },
    "read" : {
      "permissions" : [ "transfer:DescribeWorkflow" ]
    },
    "delete" : {
      "permissions" : [ "transfer:DeleteWorkflow" ]
    },
    "list" : {
      "permissions" : [ "transfer:ListWorkflows" ]
    },
    "update" : {
      "permissions" : [ "transfer:UnTagResource", "transfer:TagResource" ]
    }
  }
}