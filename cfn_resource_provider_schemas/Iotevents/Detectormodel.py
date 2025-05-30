SCHEMA = {
  "typeName" : "AWS::IoTEvents::DetectorModel",
  "description" : "The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see [How to Use](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *Developer Guide*.\n  When you successfully update a detector model (using the ITE console, ITE API or CLI commands, or CFN) all detector instances created by the model are reset to their initial states. (The detector's ``state``, and the values of any variables and timers are reset.)\n When you successfully update a detector model (using the ITE console, ITE API or CLI commands, or CFN) the version number of the detector model is incremented. (A detector model with version number 1 before the update has version number 2 after the update succeeds.)\n If you attempt to update a detector model using CFN and the update does not succeed, the system may, in some cases, restore the original detector model. When this occurs, the detector model's version is incremented twice (for example, from version 1 to version 3) and the detector instances are reset.\n Also, be aware that if you attempt to update several detector models at once using CFN, some updates may succeed and others fail. In this case, the effects on each detector model's detector instances and version number depend on whether the update succeeded or failed, with the results as stated.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "DetectorModelDefinition" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information that defines how a detector operates.",
      "properties" : {
        "InitialStateName" : {
          "type" : "string",
          "description" : "The state that is entered at the creation of each detector (instance).",
          "minLength" : 1,
          "maxLength" : 128
        },
        "States" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "description" : "Information about the states of the detector.",
          "minItems" : 1,
          "items" : {
            "$ref" : "#/definitions/State"
          }
        }
      },
      "required" : [ "States", "InitialStateName" ]
    },
    "State" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information that defines a state of a detector.",
      "properties" : {
        "OnEnter" : {
          "$ref" : "#/definitions/OnEnter",
          "description" : "When entering this state, perform these ``actions`` if the ``condition`` is TRUE."
        },
        "OnExit" : {
          "$ref" : "#/definitions/OnExit",
          "description" : "When exiting this state, perform these ``actions`` if the specified ``condition`` is ``TRUE``."
        },
        "OnInput" : {
          "$ref" : "#/definitions/OnInput",
          "description" : "When an input is received and the ``condition`` is TRUE, perform the specified ``actions``."
        },
        "StateName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "description" : "The name of the state."
        }
      },
      "required" : [ "StateName" ]
    },
    "OnEnter" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "When entering this state, perform these ``actions`` if the ``condition`` is TRUE.",
      "properties" : {
        "Events" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "description" : "Specifies the actions that are performed when the state is entered and the ``condition`` is ``TRUE``.",
          "items" : {
            "$ref" : "#/definitions/Event"
          }
        }
      }
    },
    "OnExit" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "When exiting this state, perform these ``actions`` if the specified ``condition`` is ``TRUE``.",
      "properties" : {
        "Events" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "description" : "Specifies the ``actions`` that are performed when the state is exited and the ``condition`` is ``TRUE``.",
          "items" : {
            "$ref" : "#/definitions/Event"
          }
        }
      }
    },
    "OnInput" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Specifies the actions performed when the ``condition`` evaluates to TRUE.",
      "properties" : {
        "Events" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "description" : "Specifies the actions performed when the ``condition`` evaluates to TRUE.",
          "items" : {
            "$ref" : "#/definitions/Event"
          }
        },
        "TransitionEvents" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : True,
          "description" : "Specifies the actions performed, and the next state entered, when a ``condition`` evaluates to TRUE.",
          "items" : {
            "$ref" : "#/definitions/TransitionEvent"
          }
        }
      }
    },
    "Event" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Specifies the ``actions`` to be performed when the ``condition`` evaluates to TRUE.",
      "properties" : {
        "Actions" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "description" : "The actions to be performed.",
          "items" : {
            "$ref" : "#/definitions/Action"
          }
        },
        "Condition" : {
          "type" : "string",
          "description" : "Optional. The Boolean expression that, when TRUE, causes the ``actions`` to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).",
          "maxLength" : 512
        },
        "EventName" : {
          "type" : "string",
          "description" : "The name of the event.",
          "maxLength" : 128
        }
      },
      "required" : [ "EventName" ]
    },
    "TransitionEvent" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Specifies the actions performed and the next state entered when a ``condition`` evaluates to TRUE.",
      "properties" : {
        "Actions" : {
          "type" : "array",
          "description" : "The actions to be performed.",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/Action"
          }
        },
        "Condition" : {
          "type" : "string",
          "description" : "Required. A Boolean expression that when TRUE causes the actions to be performed and the ``nextState`` to be entered.",
          "maxLength" : 512
        },
        "EventName" : {
          "type" : "string",
          "description" : "The name of the transition event.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "NextState" : {
          "type" : "string",
          "description" : "The next state to enter.",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Condition", "EventName", "NextState" ]
    },
    "Action" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An action to be performed when the ``condition`` is TRUE.",
      "properties" : {
        "ClearTimer" : {
          "$ref" : "#/definitions/ClearTimer",
          "description" : "Information needed to clear the timer."
        },
        "DynamoDB" : {
          "$ref" : "#/definitions/DynamoDB",
          "description" : "Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *Developer Guide*."
        },
        "DynamoDBv2" : {
          "$ref" : "#/definitions/DynamoDBv2",
          "description" : "Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *Developer Guide*."
        },
        "Firehose" : {
          "$ref" : "#/definitions/Firehose",
          "description" : "Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream."
        },
        "IotEvents" : {
          "$ref" : "#/definitions/IotEvents",
          "description" : "Sends ITE input, which passes information about the detector model instance and the event that triggered the action."
        },
        "IotSiteWise" : {
          "$ref" : "#/definitions/IotSiteWise",
          "description" : "Sends information about the detector model instance and the event that triggered the action to an asset property in ITSW ."
        },
        "IotTopicPublish" : {
          "$ref" : "#/definitions/IotTopicPublish",
          "description" : "Publishes an MQTT message with the given topic to the IoT message broker."
        },
        "Lambda" : {
          "$ref" : "#/definitions/Lambda",
          "description" : "Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action."
        },
        "ResetTimer" : {
          "$ref" : "#/definitions/ResetTimer",
          "description" : "Information needed to reset the timer."
        },
        "SetTimer" : {
          "$ref" : "#/definitions/SetTimer",
          "description" : "Information needed to set the timer."
        },
        "SetVariable" : {
          "$ref" : "#/definitions/SetVariable",
          "description" : "Sets a variable to a specified value."
        },
        "Sns" : {
          "$ref" : "#/definitions/Sns",
          "description" : "Sends an Amazon SNS message."
        },
        "Sqs" : {
          "$ref" : "#/definitions/Sqs",
          "description" : "Sends an Amazon SNS message."
        }
      }
    },
    "ClearTimer" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information needed to clear the timer.",
      "properties" : {
        "TimerName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "description" : "The name of the timer to clear."
        }
      },
      "required" : [ "TimerName" ]
    },
    "DynamoDB" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Defines an action to write to the Amazon DynamoDB table that you created. The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify.\n You must use expressions for all parameters in ``DynamoDBAction``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``hashKeyType`` parameter can be ``'STRING'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``hashKeyField`` parameter can be ``$input.GreenhouseInput.name``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``hashKeyValue`` parameter uses a substitution template. \n  ``'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'`` \n  +  For a string concatenation, you must use ``+``. A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``tableName`` parameter uses a string concatenation. \n  ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n If the defined payload type is a string, ``DynamoDBAction`` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the ``payloadField`` parameter is ``<payload-field>_raw``.",
      "properties" : {
        "HashKeyField" : {
          "type" : "string",
          "description" : "The name of the hash key (also called the partition key). The ``hashKeyField`` value must match the partition key of the target DynamoDB table."
        },
        "HashKeyType" : {
          "type" : "string",
          "description" : "The data type for the hash key (also called the partition key). You can specify the following values:\n  +   ``'STRING'`` - The hash key is a string.\n  +   ``'NUMBER'`` - The hash key is a number.\n  \n If you don't specify ``hashKeyType``, the default value is ``'STRING'``."
        },
        "HashKeyValue" : {
          "type" : "string",
          "description" : "The value of the hash key (also called the partition key)."
        },
        "Operation" : {
          "type" : "string",
          "description" : "The type of operation to perform. You can specify the following values: \n  +   ``'INSERT'`` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\n  +   ``'UPDATE'`` - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.\n  +   ``'DELETE'`` - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.\n  \n If you don't specify this parameter, ITE triggers the ``'INSERT'`` operation."
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "Information needed to configure the payload.\n By default, ITE generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression``."
        },
        "PayloadField" : {
          "type" : "string",
          "description" : "The name of the DynamoDB column that receives the action payload.\n If you don't specify this parameter, the name of the DynamoDB column is ``payload``."
        },
        "RangeKeyField" : {
          "type" : "string",
          "description" : "The name of the range key (also called the sort key). The ``rangeKeyField`` value must match the sort key of the target DynamoDB table."
        },
        "RangeKeyType" : {
          "type" : "string",
          "description" : "The data type for the range key (also called the sort key), You can specify the following values:\n  +   ``'STRING'`` - The range key is a string.\n  +   ``'NUMBER'`` - The range key is number.\n  \n If you don't specify ``rangeKeyField``, the default value is ``'STRING'``."
        },
        "RangeKeyValue" : {
          "type" : "string",
          "description" : "The value of the range key (also called the sort key)."
        },
        "TableName" : {
          "type" : "string",
          "description" : "The name of the DynamoDB table. The ``tableName`` value must match the table name of the target DynamoDB table."
        }
      },
      "required" : [ "HashKeyField", "HashKeyValue", "TableName" ]
    },
    "DynamoDBv2" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Defines an action to write to the Amazon DynamoDB table that you created. The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify.\n You must use expressions for all parameters in ``DynamoDBv2Action``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``tableName`` parameter can be ``'GreenhouseTemperatureTable'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``tableName`` parameter can be ``$variable.ddbtableName``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``contentExpression`` parameter in ``Payload`` uses a substitution template. \n  ``'{\\\"sensorID\\\": \\\"${$input.GreenhouseInput.sensor_id}\\\", \\\"temperature\\\": \\\"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\\\"}'`` \n  +  For a string concatenation, you must use ``+``. A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``tableName`` parameter uses a string concatenation. \n  ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n The value for the ``type`` parameter in ``Payload`` must be ``JSON``.",
      "properties" : {
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "Information needed to configure the payload.\n By default, ITE generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression``."
        },
        "TableName" : {
          "type" : "string",
          "description" : "The name of the DynamoDB table."
        }
      },
      "required" : [ "TableName" ]
    },
    "Firehose" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.",
      "properties" : {
        "DeliveryStreamName" : {
          "type" : "string",
          "description" : "The name of the Kinesis Data Firehose delivery stream where the data is written."
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to an Amazon Data Firehose delivery stream."
        },
        "Separator" : {
          "type" : "string",
          "description" : "A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).",
          "pattern" : "([\\n\\t])|(\\r\\n)|(,)"
        }
      },
      "required" : [ "DeliveryStreamName" ]
    },
    "IotEvents" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Sends an ITE input, passing in information about the detector model instance and the event that triggered the action.",
      "properties" : {
        "InputName" : {
          "type" : "string",
          "description" : "The name of the ITE input where the data is sent.",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^[a-zA-Z][a-zA-Z0-9_]*$"
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to an ITE input."
        }
      },
      "required" : [ "InputName" ]
    },
    "IotSiteWise" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Sends information about the detector model instance and the event that triggered the action to a specified asset property in ITSW.\n You must use expressions for all parameters in ``IotSiteWiseAction``. The expressions accept literals, operators, functions, references, and substitutions templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``propertyAlias`` parameter can be ``'/company/windfarm/3/turbine/7/temperature'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``assetId`` parameter can be ``$input.TurbineInput.assetId1``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``propertyAlias`` parameter uses a substitution template. \n  ``'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'`` \n  \n You must specify either ``propertyAlias`` or both ``assetId`` and ``propertyId`` to identify the target asset property in ITSW.\n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.",
      "properties" : {
        "AssetId" : {
          "type" : "string",
          "description" : "The ID of the asset that has the specified property."
        },
        "EntryId" : {
          "type" : "string",
          "description" : "A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier."
        },
        "PropertyAlias" : {
          "type" : "string",
          "description" : "The alias of the asset property."
        },
        "PropertyId" : {
          "type" : "string",
          "description" : "The ID of the asset property."
        },
        "PropertyValue" : {
          "$ref" : "#/definitions/AssetPropertyValue",
          "description" : "The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information."
        }
      },
      "required" : [ "PropertyValue" ]
    },
    "IotTopicPublish" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information required to publish the MQTT message through the IoT message broker.",
      "properties" : {
        "MqttTopic" : {
          "type" : "string",
          "description" : "The MQTT topic of the message. You can use a string expression that includes variables (``$variable.<variable-name>``) and input values (``$input.<input-name>.<path-to-datum>``) as the topic string.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you publish a message to an IoTCore topic."
        }
      },
      "required" : [ "MqttTopic" ]
    },
    "Lambda" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FunctionArn" : {
          "type" : "string",
          "description" : "The ARN of the Lambda function that is executed.",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to a Lambda function."
        }
      },
      "required" : [ "FunctionArn" ],
      "description" : "Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action."
    },
    "ResetTimer" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information required to reset the timer. The timer is reset to the previously evaluated result of the duration. The duration expression isn't reevaluated when you reset the timer.",
      "properties" : {
        "TimerName" : {
          "type" : "string",
          "description" : "The name of the timer to reset.",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "TimerName" ]
    },
    "SetTimer" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information needed to set the timer.",
      "properties" : {
        "DurationExpression" : {
          "type" : "string",
          "description" : "The duration of the timer, in seconds. You can use a string expression that includes numbers, variables (``$variable.<variable-name>``), and input values (``$input.<input-name>.<path-to-datum>``) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.",
          "minLength" : 1,
          "maxLength" : 1024
        },
        "Seconds" : {
          "type" : "integer",
          "description" : "The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.",
          "minimum" : 60,
          "maximum" : 31622400
        },
        "TimerName" : {
          "type" : "string",
          "description" : "The name of the timer.",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "TimerName" ]
    },
    "SetVariable" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information about the variable and its new value.",
      "properties" : {
        "Value" : {
          "type" : "string",
          "description" : "The new value of the variable.",
          "minLength" : 1,
          "maxLength" : 1024
        },
        "VariableName" : {
          "type" : "string",
          "description" : "The name of the variable.",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^[a-zA-Z][a-zA-Z0-9_]*$"
        }
      },
      "required" : [ "Value", "VariableName" ]
    },
    "Sns" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information required to publish the Amazon SNS message.",
      "properties" : {
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message as an Amazon SNS push notification."
        },
        "TargetArn" : {
          "type" : "string",
          "description" : "The ARN of the Amazon SNS target where the message is sent.",
          "minLength" : 1,
          "maxLength" : 2048
        }
      },
      "required" : [ "TargetArn" ]
    },
    "Sqs" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to an Amazon SQS queue."
        },
        "QueueUrl" : {
          "type" : "string",
          "description" : "The URL of the SQS queue where the data is written."
        },
        "UseBase64" : {
          "type" : "boolean",
          "description" : "Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE."
        }
      },
      "required" : [ "QueueUrl" ],
      "description" : "Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue."
    },
    "AssetPropertyValue" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A structure that contains value information. For more information, see [AssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyValue.html) in the *API Reference*.\n You must use expressions for all parameters in ``AssetPropertyValue``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``quality`` parameter can be ``'GOOD'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``quality`` parameter can be ``$input.TemperatureInput.sensorData.quality``.\n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.",
      "properties" : {
        "Quality" : {
          "type" : "string",
          "description" : "The quality of the asset property value. The value must be ``'GOOD'``, ``'BAD'``, or ``'UNCERTAIN'``."
        },
        "Timestamp" : {
          "$ref" : "#/definitions/AssetPropertyTimestamp",
          "description" : "The timestamp associated with the asset property value. The default is the current event time."
        },
        "Value" : {
          "$ref" : "#/definitions/AssetPropertyVariant",
          "description" : "The value to send to an asset property."
        }
      },
      "required" : [ "Value" ]
    },
    "AssetPropertyTimestamp" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A structure that contains timestamp information. For more information, see [TimeInNanos](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TimeInNanos.html) in the *API Reference*.\n You must use expressions for all parameters in ``AssetPropertyTimestamp``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``timeInSeconds`` parameter can be ``'1586400675'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``offsetInNanos`` parameter can be ``$variable.time``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``timeInSeconds`` parameter uses a substitution template.\n  ``'${$input.TemperatureInput.sensorData.timestamp / 1000}'`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.",
      "properties" : {
        "OffsetInNanos" : {
          "type" : "string",
          "description" : "The nanosecond offset converted from ``timeInSeconds``. The valid range is between 0-999999999."
        },
        "TimeInSeconds" : {
          "type" : "string",
          "description" : "The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199."
        }
      },
      "required" : [ "TimeInSeconds" ]
    },
    "AssetPropertyVariant" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A structure that contains an asset property value. For more information, see [Variant](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Variant.html) in the *API Reference*.\n You must use expressions for all parameters in ``AssetPropertyVariant``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``integerValue`` parameter can be ``'100'``.\n  +  For references, you must specify either variables or parameters. For example, the value for the ``booleanValue`` parameter can be ``$variable.offline``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. \n In the following example, the value for the ``doubleValue`` parameter uses a substitution template. \n  ``'${$input.TemperatureInput.sensorData.temperature * 6 / 5 + 32}'`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n You must specify one of the following value types, depending on the ``dataType`` of the specified asset property. For more information, see [AssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetProperty.html) in the *API Reference*.",
      "properties" : {
        "BooleanValue" : {
          "type" : "string",
          "description" : "The asset property value is a Boolean value that must be ``'TRUE'`` or ``'FALSE'``. You must use an expression, and the evaluated result should be a Boolean value."
        },
        "DoubleValue" : {
          "type" : "string",
          "description" : "The asset property value is a double. You must use an expression, and the evaluated result should be a double."
        },
        "IntegerValue" : {
          "type" : "string",
          "description" : "The asset property value is an integer. You must use an expression, and the evaluated result should be an integer."
        },
        "StringValue" : {
          "type" : "string",
          "description" : "The asset property value is a string. You must use an expression, and the evaluated result should be a string."
        }
      }
    },
    "Payload" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information needed to configure the payload.\n By default, ITE generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression``.",
      "properties" : {
        "ContentExpression" : {
          "type" : "string",
          "description" : "The content of the payload. You can use a string expression that includes quoted strings (``'<string>'``), variables (``$variable.<variable-name>``), input values (``$input.<input-name>.<path-to-datum>``), string concatenations, and quoted strings that contain ``${}`` as the content. The recommended maximum size of a content expression is 1 KB.",
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "description" : "The value of the payload type can be either ``STRING`` or ``JSON``."
        }
      },
      "required" : [ "ContentExpression", "Type" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Metadata that can be used to manage the resource.",
      "properties" : {
        "Key" : {
          "description" : "The tag's key.",
          "type" : "string"
        },
        "Value" : {
          "description" : "The tag's value.",
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "DetectorModelDefinition" : {
      "$ref" : "#/definitions/DetectorModelDefinition",
      "description" : "Information that defines how a detector operates."
    },
    "DetectorModelDescription" : {
      "type" : "string",
      "description" : "A brief description of the detector model.",
      "maxLength" : 1024
    },
    "DetectorModelName" : {
      "type" : "string",
      "description" : "The name of the detector model.",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "EvaluationMethod" : {
      "type" : "string",
      "description" : "Information about the order in which events are evaluated and how actions are executed.",
      "enum" : [ "BATCH", "SERIAL" ]
    },
    "Key" : {
      "type" : "string",
      "description" : "The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. ITE can continue to route input to its corresponding detector instance based on this identifying information. \n This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "^((`[\\w\\- ]+`)|([\\w\\-]+))(\\.((`[\\w\\- ]+`)|([\\w\\-]+)))*$"
    },
    "RoleArn" : {
      "type" : "string",
      "description" : "The ARN of the role that grants permission to ITE to perform its operations.",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource.\n For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "DetectorModelDefinition", "RoleArn" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/DetectorModelName" ],
  "createOnlyProperties" : [ "/properties/DetectorModelName", "/properties/Key" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotevents:CreateDetectorModel", "iotevents:UpdateInputRouting", "iotevents:DescribeDetectorModel", "iotevents:ListTagsForResource", "iotevents:TagResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "iotevents:DescribeDetectorModel", "iotevents:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotevents:UpdateDetectorModel", "iotevents:UpdateInputRouting", "iotevents:DescribeDetectorModel", "iotevents:ListTagsForResource", "iotevents:UntagResource", "iotevents:TagResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "iotevents:DeleteDetectorModel", "iotevents:DescribeDetectorModel" ]
    },
    "list" : {
      "permissions" : [ "iotevents:ListDetectorModels" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotevents:UntagResource", "iotevents:TagResource", "iotevents:ListTagsForResource" ]
  }
}